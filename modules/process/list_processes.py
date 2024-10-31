
from enum import Enum

from modules.process.models.create_warehouse_turnovers import create_warehouse_turnovers as Create_warehouse_turnovers


class list_processes(Enum):

    create_warehouse_turnovers = Create_warehouse_turnovers
