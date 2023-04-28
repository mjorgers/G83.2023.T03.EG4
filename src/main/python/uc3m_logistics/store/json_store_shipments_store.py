"""Contains the class JsonStoreShipmentsStore"""
from uc3m_logistics.config.order_manager_config import JSON_FILES_PATH
# pylint: disable=relative-beyond-top-level
from .json_store_master import JsonStoreMaster


# pylint: disable=too-few-public-methods
class JsonStoreShipmentsStore(JsonStoreMaster):
    """Clase JsonStoreShipmentsStore"""
    _FILE_PATH = JSON_FILES_PATH + "shipments_store.json"
    _ID_FIELD = "_OrderShipping__tracking_code"
    _data_list = []

    def __init__(self):
        # pylint: disable=useless-parent-delegation
        super().__init__()

    # pylint: disable=too-few-public-methods
    def add_item(self, item):
        """Añadimos item"""
        self.load_store()
        self._data_list.append(item.__dict__)
        self.save_store()
