from enum import Enum

class event_type(Enum):
    SAVE_DATA_REPOSITY = 1
    READ_DATA_REPOSITY = 2
    ERROR = 3
    WEB = 4
    INFO = 5
    SETTINGS = 6
    STORAGE = 7
    GET_NOMENCLATURE = 8
    PUT_NOMENCLATURE = 9
    PATCH_NOMENCLATURE = 10
    DELETE_NOMENCLATURE = 11
