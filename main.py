
from modules.settings.settings_base import Settings
from modules.settings.settings_manager import Settings_manager

def go_from_win_to_utf(s: str):
    return s.encode('windows-1251').decode('utf-8')

manager1 = Settings_manager()
if not manager1.open("settings1.json", file_path=r"C:\git\Design_patterns\data"):
    print("Настройки не загружены!")

print(f"settings1: {manager1.settings}")

manager2 = Settings_manager()

print(f"settings2: {manager2.settings}")

# 1 При отключенном методе __new__
# settings1: Рога и копыта
# settings2: Рога и копыта (default)

# 2 При включенном методе __new__
# settings1: Рога и копыта
# settings2: Рога и копыта




