"""Contains the class OrderManager"""
import datetime
import re
import json
from datetime import datetime
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
from .order_manager_config import JSON_FILES_PATH
from.json_store import JsonStore

class OrderManager:
    """Class for providing the methods for managing the orders process"""

    def __init__(self):
        pass

    @staticmethod
    def validate_tracking_code(tracking_code: str) -> None:
        """Method for validating sha256 values"""
        myregex = re.compile(r"[0-9a-fA-F]{64}$")
        result = myregex.fullmatch(tracking_code)
        if not result:
            raise OrderManagementException("tracking_code format is not valid")

    @staticmethod
    def save_fast(order_request: OrderRequest) -> None:
        """Method for saving the orders store"""
        orders_store = JSON_FILES_PATH + "orders_store.json"
        with open(orders_store, "r+", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
            data_list.append(order_request.__dict__)
            file.seek(0)
            json.dump(data_list, file, indent=2)

    # pylint: disable=too-many-arguments
    def register_order(self,
                       product_id: str,
                       order_type: str,
                       address: str,
                       phone_number: str,
                       zip_code: str) -> str:
        """Register the orders into the order's file"""

        my_order = OrderRequest(product_id,
                                order_type,
                                address,
                                phone_number,
                                zip_code)

        my_store = JsonStore()
        my_store.save_store(my_order)

        return my_order.order_id

    # pylint: disable=too-many-locals
    def send_product(self, input_file: str) -> str:
        """Sends the order included in the input_file"""

        my_sign = OrderShipping(input_file)
        my_store = JsonStore()
        my_store.save_orders_shipped(my_sign)

        return my_sign.tracking_code

    def deliver_product(self, tracking_code: str) -> bool:
        """Register the delivery of the product"""
        self.validate_tracking_code(tracking_code)

        # check if this tracking_code is in shipments_store
        my_store = JsonStore()
        data_list = my_store.read_shipping_store()

        # search this tracking_code
        del_timestamp = my_store.find_tracking_code(data_list, tracking_code)
        self.check_date(del_timestamp)

        my_store.save_delivere_store(tracking_code)
        return True

    def check_date(self, del_timestamp):
        """Check the date"""
        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")
