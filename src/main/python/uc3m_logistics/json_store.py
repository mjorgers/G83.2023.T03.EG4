"""Contains the class JsonStore"""
import json
from.order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_manager_config import JSON_FILES_PATH
class JsonStore():
    """Creamos esta clase para los store"""
    def __init__(self):
        pass

    @staticmethod
    def save_store(order_request: OrderRequest) -> bool:
        """Medthod for saving the orders store"""
        file_store = JSON_FILES_PATH + "orders_store.json"
        # first read the file
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == order_request.order_id:
                found = True
        if found is False:
            data_list.append(order_request.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex
        return True
