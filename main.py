
import connexion

from modules.data_reposity import data_reposity
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


@app.route("/api/reports/formats", methods=["GET"])
def formats():
    return [{"name": item.name, "value": item.value} for item in format_reporting]

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


if __name__ == '__main__':
    app.add_api("swagger.yaml")
    app.run(port = 8080)