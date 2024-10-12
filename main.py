import connexion
from flask import request

from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filter_objects import filter_objects
from modules.Dto.filtration_type import filtration_type
from modules.data_key import data_key
from modules.data_reposity import data_reposity
from modules.prototype.prototype import prototype
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service
from modules.reports.format_reporting import format_reporting
from modules.reports.report_manager import Report_manager

app = connexion.FlaskApp(__name__)

manager = Settings_manager()
manager.open("settings.json")
manager.open_report_settings("reports.json")
reposity = data_reposity()
start = start_service(reposity, manager)
start.create()

report_manager = Report_manager()

f_m = Filter_manager()
f_m.update_filter_property()
f_m.update_filter()


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
    return f_m.filter_property


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


@app.route("/api/filter/<string:domain>", methods=["POST"])
def filter_data(domain):
    json_data = request.json

    f_m.update_filter_property()
    f_m.update_filter()
    f_m.update_property_filter(**json_data)
    data = reposity.data[list(data_key)[int(domain)].value]
    p = prototype()

    new_data = p.create(data, f_m.filter, f_m.filter_property).data
    return f"{new_data}"

if __name__ == '__main__':
    app.add_api("swagger.yaml")
    app.run(port = 8080)

