
from enum import Enum

from modules.process.models.create_warehouse_turnovers import create_warehouse_turnovers as Create_warehouse_turnovers
from modules.process.models.read_result_turnovers import read_result_turnovers as Read_result_turnovers
from modules.process.models.save_result_turnovers import save_result_turnovers as Save_result_turnovers


class list_processes(Enum):

    create_warehouse_turnovers = Create_warehouse_turnovers
    read_result_turnovers = Read_result_turnovers
    save_result_turnover = Save_result_turnovers

