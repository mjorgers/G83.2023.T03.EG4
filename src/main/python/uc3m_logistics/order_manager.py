"""Contains the class OrderManager"""
from .order_request import OrderRequest
from .order_shipping import OrderShipping
from.json_store import JsonStore
from .order_delivered import OrderDelivered

class OrderManager:
    """Class for providing the methods for managing the orders process"""

    def __init__(self):
        pass

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
        my_deliver = OrderDelivered(tracking_code)

        # check if this tracking_code is in shipments_store
        my_store = JsonStore()
        data_list = my_store.read_shipping_store()

        # search this tracking_code
        del_timestamp = my_store.find_tracking_code(data_list, tracking_code)
        my_deliver.check_date(del_timestamp)

        my_store.save_delivere_store(my_deliver)
        return True
