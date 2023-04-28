"""Contains the class JsonStoreShipmentsDelivered"""
import json
from uc3m_logistics.config.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.exception.order_management_exception import OrderManagementException
# pylint: disable=relative-beyond-top-level
from .json_store_master import JsonStoreMaster


class JsonStoreShipmentsDelivered(JsonStoreMaster):
    """Clase JsonStoreShipmentsDelivered"""
    _FILE_PATH1 = JSON_FILES_PATH + "shipments_store.json"
    _FILE_PATH2 = JSON_FILES_PATH + "shipments_delivered.json"
    _ID_FIELD1 = "_OrderShipping__tracking_code"
    _ID_FIELD2 = "_OrderShipping__delivery_day"
    _data_list = []

    def __init__(self):
        # pylint: disable=useless-parent-delegation
        super().__init__()

    def read_shipping_store(self):
        """Leemos shipping_store"""
        # first read the file
        try:
            with open(self._FILE_PATH1, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        except FileNotFoundError as ex:
            raise OrderManagementException("shipments_store not found") from ex

    def find_tracking_code(self, tracking_code):
        """Encontramos tracking_code"""
        found = False
        del_timestamp = ""
        for item in self._data_list:
            if item[self._ID_FIELD1] == tracking_code:
                found = True
                del_timestamp = item[self._ID_FIELD2]
        if not found:
            raise OrderManagementException("tracking_code is not found")
        return del_timestamp

    def save_store_delivere(self):
        """Guardamos data"""
        try:
            with open(self._FILE_PATH2, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

    def save_delivere_store(self, tracking_code):
        """Guardamos delivere_store"""
        with open(self._FILE_PATH2, "r", encoding="utf-8", newline="") as file:
            self._data_list = json.load(file)

        # append the delivery info
        self._data_list.append(tracking_code.__dict__)
        self.save_store_delivere()

    def add_item(self, item):
        """Añadimos item"""
        self.load_store()
        self.read_shipping_store()
        del_timestamp = self.find_tracking_code(item.tracking_code)
        return del_timestamp
