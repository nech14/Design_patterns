
from enum import Enum

from modules.process.processes.create_warehouse_turnovers import create_warehouse_turnovers as Create_warehouse_turnovers
from modules.process.processes.read_result_turnovers import read_result_turnovers as Read_result_turnovers
from modules.process.processes.save_result_turnovers import save_result_turnovers as Save_result_turnovers
from modules.process.processes.create_warehouse_turnovers_date import create_warehouse_turnovers_date as Create_warehouse_turnovers_date
from modules.process.processes.update_warehouse_turnovers_block_period import update_warehouse_turnovers_block_period as Update_warehouse_turnovers_block_period
from modules.process.processes.create_TBS import create_TBS as Create_TBS
from modules.process.processes.print_log_process import print_log_process as Print_log_process
from modules.process.processes.save_log_process import save_log_process as Save_log_process


class list_processes(Enum):

    create_warehouse_turnovers = Create_warehouse_turnovers
    read_result_turnovers = Read_result_turnovers
    save_result_turnover = Save_result_turnovers
    create_warehouse_turnovers_date = Create_warehouse_turnovers_date
    update_warehouse_turnovers_block_period = Update_warehouse_turnovers_block_period
    create_TBS = Create_TBS
    print_log_process = Print_log_process
    save_log_process = Save_log_process

