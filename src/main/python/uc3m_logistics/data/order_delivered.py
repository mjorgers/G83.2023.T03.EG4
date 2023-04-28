"""Contains the class OrderDelivered"""
from datetime import datetime
from uc3m_logistics.exception.order_management_exception import OrderManagementException
from uc3m_logistics.data.data_attr.attribute_tracking_code import TrackingCode
class OrderDelivered():
    """OrderDelivered"""
    def __init__(self, tracking_code):
        self.__tracking_code = TrackingCode(tracking_code).value
        self.__date_delivered = str(datetime.utcnow())

    @property
    def tracking_code( self ):
        """Property representing the tracking_code"""
        return self.__tracking_code

    @tracking_code.setter
    def tracking_code( self, value ):
        self.__tracking_code = value

    @property
    def date_delivered( self ):
        """Property representing the date_delivered"""
        return self.__date_delivered
    @date_delivered.setter
    def date_delivered( self, value ):
        self.__date_delivered = value

    def check_date(self, del_timestamp):
        """Check the date"""
        today = datetime.today().date()
        delivery_date = datetime.fromtimestamp(del_timestamp).date()
        if delivery_date != today:
            raise OrderManagementException("Today is not the delivery date")
