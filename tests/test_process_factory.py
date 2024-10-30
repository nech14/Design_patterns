import unittest
from datetime import datetime, timedelta
import time

from matplotlib import pyplot as plt

from modules.Dto.filter_manager import Filter_manager
from modules.Dto.filtration_type import filtration_type
from modules.data_reposity import data_reposity
from modules.models.warehouse_transaction_model import warehouse_transaction_model
from modules.models.warehouse_turnover_model import warehouse_turnover_model
from modules.process.list_processes import list_processes
from modules.process.modified_list import modified_list
from modules.process.process_factory import Process_factory
from modules.prototype.prototype import prototype
from modules.settings.settings_manager import Settings_manager
from modules.start_service import start_service


class Test_process_factory(unittest.TestCase):
    manager = Settings_manager()
    manager.open("settings.json", r"..\\data\\")
    manager.open_report_settings("../reports.json")
    reposity = data_reposity()
    start = start_service(reposity, manager)
    start.create()



    def test_create_warehouse_turnovers(self):
        #preparation
        item_process_factory = Process_factory()

        data = modified_list(self.reposity.data[self.reposity.warehouse_transaction_key()])

        result = item_process_factory.start_process(data, list_processes.create_warehouse_turnovers.name)
        result:list[warehouse_turnover_model]

        #test the creation of a normal quantity
        self.assertEqual(
            len(result),
            2
        )

        #test the work transaction_type
        self.assertEqual(
            result[0].turnover,
            1
        )


    def test_speed(self):

        start_date = datetime(1990, 1, 1)
        number_of_days = 1
        count = 100000

        list_transaction = []
        for i in range(count):
            item_warehouse_transaction = warehouse_transaction_model.get_base_warehouse_transaction(
                period=start_date + timedelta(days=i*number_of_days)
            )
            list_transaction.append(item_warehouse_transaction)

        end_date = start_date + timedelta(days=count*number_of_days)
        # end_date = end_date.date()

        process_factory = Process_factory()
        prototype_obj = prototype()
        filter_manager = Filter_manager()

        # Вычисляем 10 равных промежутков между двумя датами
        dates_i = [start_date + (end_date - start_date) * i / 9 for i in range(10)]
        dates = [start_date + (end_date - start_date) * i / 49 for i in range(50)]
        block_period = dates[0].replace(hour=0, minute=0, second=0, microsecond=0)

        first_filter_dict = {
            "period": [
                datetime(1990, 1, 1),
                block_period
            ]
        }

        filter_manager.update_filter_from_dict(first_filter_dict)

        list_block_period = prototype_obj.create(
            list_transaction,
            filter_manager.filter,
            filter_manager.filter_property,
            filtration_type.INTERVAL
        ).data



        result = process_factory.start_process(
            modified_list(list_block_period),
            list_processes.create_warehouse_turnovers.name
        )

        with open("../result/speed_test_result.md", 'w') as f:
            f.write(f"# Result for {count} transactions\n\n")
            f.write("| block_period  | time in seconds |\n")
            f.write("| ------------  | --------------- |\n")


        buf_time = []
        for i in range(len(dates_i)-2):
            dates_x = []
            result_time = []

            for date in dates:

                first_filter_dict = {
                    "period": [
                        block_period,
                        date.replace(hour=0, minute=0, second=0, microsecond=0)
                    ]
                }
                filter_manager.update_filter_from_dict(first_filter_dict)



                list_new_period = prototype_obj.create(
                    list_transaction,
                    filter_manager.filter,
                    filter_manager.filter_property,
                    filtration_type.INTERVAL
                ).data

                # Запись времени начала
                start_time = time.time()

                if len(list_new_period) > 0:
                    new_result = process_factory.start_process(
                        list_new_period,
                        list_processes.create_warehouse_turnovers.name
                    )

                    final_result = result + new_result
                else:
                    final_result = result

                # Запись времени окончания
                end_time = time.time()

                # Вычисление времени выполнения
                execution_time = end_time - start_time
                result_time.append(execution_time)

                dates_x.append((date-start_date).days/number_of_days)

                # print(f"Время выполнения: {execution_time:.6f} секунд")


            x_values = [i for i in range(len(result_time))]
            plt.plot(dates_x,  result_time, label=f"{block_period.date()}")

            with open("../result/speed_test_result.md", 'a') as f:
                f.write(f"| {block_period.date()}  | {result_time[-1]} |\n")


            block_period = dates_i[i+1].replace(hour=0, minute=0, second=0, microsecond=0)
            first_filter_dict = {
                "period": [
                    dates[i],
                    block_period
                ]
            }

            filter_manager.update_filter_from_dict(first_filter_dict)

            list_block_period = prototype_obj.create(
                list_transaction,
                filter_manager.filter,
                filter_manager.filter_property,
                filtration_type.INTERVAL
            ).data

            result += process_factory.start_process(
                modified_list(list_block_period),
                list_processes.create_warehouse_turnovers.name
            )
        plt.title(f"test speed on date:{start_date.date()}-{end_date.date()}")
        plt.xlabel(f"count_transaction ")
        plt.ylabel(f"time in seconds")
        plt.legend()
        plt.savefig("../result/test_speed.png")
        plt.close()

