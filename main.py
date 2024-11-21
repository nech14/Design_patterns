import json

from datetime import datetime


import connexion
import jsonpickle
from flask import request

from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filter_objects import filter_objects
from modules.Dto.filtration_type import filtration_type
from modules.Enums.data_key import data_key
from modules.Enums.event_type import event_type
from modules.creator_manager import Creator_manager
from modules.data_reposity import data_reposity
from modules.models.nomenclature_model import nomenclature_model
from modules.models.warehouse_model import warehouse_model
from modules.observers.observer_update_nomenclature import observer_update_nomenclature
from modules.process.list_processes import list_processes
from modules.process.modified_list import modified_list
from modules.process.process_factory import Process_factory
from modules.prototype.prototype import prototype
from modules.service.nomenclature_service import nomenclature_service as Nomenclature_service
from modules.service.observer_service import observe_service
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service
from modules.reports.format_reporting import format_reporting
from modules.reports.report_manager import Report_manager

app = connexion.FlaskApp(__name__)

manager = Settings_manager()
manager.open("settings.json", "data")
manager.open_report_settings("reports.json")
reposity = data_reposity()
start = start_service(reposity, manager)
start.create()

report_manager = Report_manager()

filter_manager = Filter_manager()
filter_manager.update_filter_property()
filter_manager.update_filter()

nomenclature_service = Nomenclature_service()
nomenclature_service.data_reposity = reposity

nomenclature_observer = observer_update_nomenclature()
nomenclature_observer.data_reposity = reposity

nomenclature_service.add_observer(nomenclature_observer)

creator_manager = Creator_manager()



@app.route("/api/reports/formats", methods=["GET"])
def formats():
    return [{"name": item.name, "value": item.value} for item in format_reporting]

@app.route("/api/filter/formats", methods=["GET"])
def filter_format():
    return [{"name": item.name} for item in filter_objects]

@app.route("/api/filter/type", methods=["GET"])
def filter_type():
    return [{"name": item.name, "value": item.value} for item in filtration_type]


@app.route("/api/filter/base/property", methods=["GET"])
def filter_base_property():
    return filter_manager.filter_property


@app.route("/api/reports/range/<format>", methods=["GET"])
def reports_range(format: str):
    report_manager.format = format_reporting(int(format))
    report_manager.create(
        start.reposity.data[data_reposity.range_key()]
    )
    report = report_manager.report

    return report.result

@app.route("/api/reports/group/<format>", methods=["GET"])
def reports_group(format: str):
    report_manager.format = format_reporting(int(format))
    report_manager.create(
        start.reposity.data[data_reposity.group_key()]
    )
    report = report_manager.report

    return report.result


@app.route("/api/reports/nomenclature/<format>", methods=["GET"])
def reports_nomenclature(format: str):
    report_manager.format = format_reporting(int(format))
    report_manager.create(
        start.reposity.data[data_reposity.nomenclature_key()]
    )
    report = report_manager.report

    return report.result

@app.route("/api/reports/receipt/<format>", methods=["GET"])
def reports_receipt(format: str):
    report_manager.format = format_reporting(int(format))
    report_manager.create(
        start.reposity.data[data_reposity.receipt_key()]
    )
    report = report_manager.report

    return report.result


@app.route("/api/filter/list/<string:domain>/<string:filter_type>", methods=["POST"])
def filter_data_list(domain, filter_type):
    json_data = request.json

    filter_manager.update_filter_property()
    filter_manager.update_filter()
    filter_manager.update_property_filter(**json_data)
    data = reposity.data[list(data_key)[int(domain)].value]
    p = prototype()

    new_data = p.create(data, filter_manager.filter, filter_manager.filter_property, filtration_type(int(filter_type))).data
    return f"{new_data}"



@app.route("/api/filter/dict/<string:domain>/<string:filter_type>", methods=["POST"])
def filter_data_dict(domain, filter_type):
    json_data = request.json
    filter_dict = json.loads(json_data)


    filter_manager.update_filter_from_dict(filter_dict)
    data = reposity.data[list(data_key)[int(domain)].value]
    p = prototype()

    new_data = p.create(data, filter_manager.filter, filter_manager.filter_property, filtration_type(int(filter_type))).data
    return f"{new_data}"



@app.route("/api/warehouse_turnover/<string:filter_type>/<string:date>", methods=["POST"])
def get_warehouse_turnover(filter_type, date):
    filter_types_names = [member.name for member in filtration_type]
    if not filter_type in filter_types_names:
        return f"such a filter({filter_type}) is not implemented", 400

    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except Exception as e:
        return f"{e}", 400


    data_filer = request.get_json()

    filter_dict = {}

    if data_filer["warehouse"] != {}:
        filter_warehouse: warehouse_model = jsonpickle.decode(json.dumps(data_filer["warehouse"]))
        filter_dict["warehouse.address"] = filter_warehouse.address
        filter_dict["warehouse.name"] = filter_warehouse.name
    if data_filer["nomenclature"] != {}:
        filter_nomenclature: nomenclature_model = jsonpickle.decode(json.dumps(data_filer["nomenclature"]))
        filter_dict["nomenclature.name"] = filter_nomenclature.name
        filter_dict["nomenclature.group.name"] = filter_nomenclature.group.name
        filter_dict["nomenclature.range.name"] = filter_nomenclature.range.name

    process_factory = Process_factory()
    prototype_obj = prototype()
    filter_manager = Filter_manager()

    items_warehouse_transaction = reposity.data[reposity.warehouse_transaction_key()]
    items_warehouse_transaction = modified_list(items_warehouse_transaction)
    items_warehouse_transaction.block_period = manager.settings.block_period
    items_warehouse_transaction.date = date

    new_data = process_factory.start_process(
        data=items_warehouse_transaction,
        process=list_processes.create_warehouse_turnovers_date.name
    )

    filter_manager.update_filter_from_dict(filter_dict)

    filtered_data = prototype_obj.create(
        new_data,
        filter_manager.filter,
        filter_manager.filter_property,
        filtration_type[filter_type]
    ).data

    return f"{filtered_data}"


@app.route("/api/warehouse_transaction/<string:filter_type>", methods=["POST"])
def get_warehouse_transaction(filter_type):

    filter_types_names = [member.name for member in filtration_type]
    if not filter_type in filter_types_names:
        return f"such a filter({filter_type}) is not implemented", 400

    data_filer = request.get_json()

    filter_dict = {}

    if data_filer["warehouse"] != {}:
        filter_warehouse: warehouse_model = jsonpickle.decode(json.dumps(data_filer["warehouse"]))
        filter_dict["warehouse.address"] = filter_warehouse.address
        filter_dict["warehouse.name"] = filter_warehouse.name
    if data_filer["nomenclature"] != {}:
        filter_nomenclature: nomenclature_model = jsonpickle.decode(json.dumps(data_filer["nomenclature"]))
        filter_dict["nomenclature.name"] = filter_nomenclature.name
        filter_dict["nomenclature.group.name"] = filter_nomenclature.group.name
        filter_dict["nomenclature.range.name"] = filter_nomenclature.range.name


    data = reposity.data[reposity.warehouse_transaction_key()]

    prototype_obj = prototype()

    filter_manager = Filter_manager()
    filter_manager.update_filter_from_dict(filter_dict)

    filtered_data = prototype_obj.create(
        data,
        filter_manager.filter,
        filter_manager.filter_property,
        filtration_type[filter_type]
    ).data

    return f"{filtered_data}"



@app.route("/api/block_period", methods=["GET"])
def get_block_period():
    return f"{manager.settings.block_period.date()}"



@app.route("/api/block_period/save", methods=["GET"])
def save_block_period():

    manager.save_block_period("data/settings.json")
    try:
        return True, 200
    except:
        return False, 500


@app.route("/api/block_period/<string:block_period>", methods=["POST"])
def update_block_period(block_period):
    try:
        last_block_period = manager.settings.block_period
        manager.settings.block_period = block_period

        process_factory = Process_factory()

        items_warehouse_transaction = reposity.data[reposity.warehouse_transaction_key()]
        items_warehouse_transaction = modified_list(items_warehouse_transaction)
        items_warehouse_transaction.block_period = last_block_period
        items_warehouse_transaction.date = manager.settings.block_period


        status = process_factory.start_process(
            items_warehouse_transaction,
            list_processes.update_warehouse_turnovers_block_period.name
        )

        return f"{status}", 200
    except Exception as e:
        return f"Exception: {e}", 400


@app.route("/api/nomenclature/get/<string:item_id>", methods=["GET"])
def nomenclature_get(item_id: str):
    result = nomenclature_service.get_item(item_id)

    return f"{result}", 200


@app.route("/api/nomenclature/put", methods=["POST"])
def nomenclature_put():
    data_filer = request.get_json()
    item = Creator_manager(data_filer).get_object()
    result = nomenclature_service.put_item(item)

    return result


@app.route("/api/nomenclature/patch", methods=["POST"])
def nomenclature_patch():
    data_filer = request.get_json()
    creator_manager.get_object(data_filer)
    item = creator_manager.object
    result = nomenclature_service.path_item(item)

    return result



@app.route("/api/nomenclature/delete/<string:item_id>", methods=["GET"])
def nomenclature_delete(item_id: str):
    result = nomenclature_service.delete_item(item_id)

    return result


@app.route("/api/tbs/<string:start_date>/<string:end_date>/<string:warehouse>", methods=["GET"])
def get_TBS(start_date: str, end_date: str, warehouse:str):
    data = reposity.data[data_reposity.warehouse_transaction_key()]

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    _filter = {
        "period": [
                datetime(1900, 1, 1),
                end_date
        ]
    }

    filter_manager = Filter_manager()
    filter_manager.update_filter_from_dict(_filter)

    prototype_obj = prototype()

    filter_data = prototype_obj.create(
        data,
        filter_manager.filter,
        filter_manager.filter_property,
        filtration_type.INTERVAL
    ).data


    _filter = {
        "warehouse": warehouse
    }

    filter_manager.update_filter_from_dict(_filter)

    filter_data = prototype_obj.create(
        filter_data,
        filter_manager.filter,
        filter_manager.filter_property,
        filtration_type.EQUALS
    ).data

    filter_data = modified_list(filter_data)
    filter_data.date = start_date

    process = Process_factory()
    tbs = process.start_process(filter_data, list_processes.create_TBS.name)

    return json.loads(f"{tbs}")



@app.route("/api/data_reposity/save", methods=["POST"])
def save_data_reposity():
    try:
        observe_service.raise_event(event=event_type.SAVE_DATA_REPOSITY, data=data_reposity)
        manager.settings.first_start = False
        return 200
    except:
        return 500


@app.route("/api/data_reposity/read", methods=["POST"])
def read_data_reposity():
    try:
        observe_service.raise_event(event=event_type.READ_DATA_REPOSITY, data=data_reposity)
        return 200
    except:
        return 500



if __name__ == '__main__':
    app.add_api("swagger.yaml")
    app.run(host="0.0.0.0", port = 8080)

