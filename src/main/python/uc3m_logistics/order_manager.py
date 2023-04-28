"""Contains the class OrderManager"""
from uc3m_logistics.data.order_request import OrderRequest
from uc3m_logistics.data.order_shipping import OrderShipping
from uc3m_logistics.data.order_delivered import OrderDelivered
from uc3m_logistics.store.json_store_orders import JsonStoreOrders
from uc3m_logistics.store.json_store_shipments_store import JsonStoreShipmentsStore
from uc3m_logistics.store.json_store_shipments_delivered import JsonStoreShipmentsDelivered


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

        my_store = JsonStoreOrders()
        my_store.add_item(my_order)

        return my_order.order_id

    # pylint: disable=too-many-locals
    def send_product(self, input_file: str) -> str:
        """Sends the order included in the input_file"""

        my_sign = OrderShipping(input_file)
        my_store = JsonStoreShipmentsStore()
        my_store.add_item(my_sign)

        return my_sign.tracking_code

    def deliver_product(self, tracking_code: str) -> bool:
        """Register the delivery of the product"""
        my_deliver = OrderDelivered(tracking_code)

        # check if this tracking_code is in shipments_store
        my_store = JsonStoreShipmentsDelivered()
        del_timestamp = my_store.add_item(my_deliver)
        my_deliver.check_date(del_timestamp)
        my_store.save_delivere_store(my_deliver)
        return True
