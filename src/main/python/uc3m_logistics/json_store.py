"""Contains the class JsonStore"""
import json
from datetime import datetime
from.order_request import OrderRequest
from.order_shipping import OrderShipping
from .order_management_exception import OrderManagementException
from .order_manager_config import JSON_FILES_PATH
class JsonStore():
    """Creamos esta clase para los store"""
    def __init__(self):
        pass


    def save_store(self, order_request: OrderRequest) -> bool:
        """Medthod for saving the orders store"""
        file_store = JSON_FILES_PATH + "orders_store.json"
        # first read the file
        data_list = self.load_store(file_store)

        found = self.find_data(order_request, data_list)
        if found is False:
            data_list.append(order_request.__dict__)
        else:
            raise OrderManagementException("order_id is already registered in orders_store")
        self.save_data(data_list, file_store)
        return True

    def save_data(self, data_list, file_store):
        """Guardamos data"""
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

    def find_data(self, order_request, data_list):
        """Encontramos data"""
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == order_request.order_id:
                found = True
        return found

    def load_store(self, file_store):
        """Cargamos data"""
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data_list


    def save_orders_shipped(self, shipment: OrderShipping) -> None:
        """Saves the shipping object into a file"""
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        data_list = self.load_store(shimpents_store_file)

        # append the shipments list
        data_list.append(shipment.__dict__)
        self.save_data(data_list, shimpents_store_file)

    def read_shipping_store(self):
        """Leemos shipping_store"""
        shimpents_store_file = JSON_FILES_PATH + "shipments_store.json"
        # first read the file
        try:
            with open(shimpents_store_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError as ex:
            raise OrderManagementException("shipments_store not found") from ex
        return data_list

    def find_tracking_code(self, data_list, tracking_code):
        """Encontramos tracking_code"""
        found = False
        for item in data_list:
            if item["_OrderShipping__tracking_code"] == tracking_code:
                found = True
                del_timestamp = item["_OrderShipping__delivery_day"]
        if not found:
            raise OrderManagementException("tracking_code is not found")
        return del_timestamp

    def save_delivere_store(self, tracking_code):
        """Guardamos delivere_store"""
        shipments_file = JSON_FILES_PATH + "shipments_delivered.json"
        try:
            with open(shipments_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

            # append the delivery info
        data_list.append(str(tracking_code))
        data_list.append(str(datetime.utcnow()))
        self.save_data(data_list, shipments_file)
