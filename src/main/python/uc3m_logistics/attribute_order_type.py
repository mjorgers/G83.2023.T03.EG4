"""module"""
from .attribute import Attribute


class OrderType(Attribute):
    """order_type"""
    def __init__(self, attr_value):
        super().__init__()
        self._error_message = "order_type is not valid"
        self._validation_pattern = r"(Regular|Premium)"
        self._attr_value = self._validate(attr_value)
