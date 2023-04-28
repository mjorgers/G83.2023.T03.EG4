"""Contains the class JsonStoreShipmentsStore"""
from .json_store_master import JsonStoreMaster
from .order_manager_config import JSON_FILES_PATH


class JsonStoreShipmentsStore(JsonStoreMaster):
    """Clase JsonStoreShipmentsStore"""
    _FILE_PATH = JSON_FILES_PATH + "shipments_store.json"
    _ID_FIELD = "_OrderShipping__tracking_code"
    _data_list = []

    def __init__(self):
        pass

    def add_item(self, item):
        """Añadimos item"""
        self.load_store()
        self._data_list.append(item.__dict__)
        self.save_store()
