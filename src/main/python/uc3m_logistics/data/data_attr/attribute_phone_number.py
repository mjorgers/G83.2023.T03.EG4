"""module"""
# pylint: disable=relative-beyond-top-level
from .attribute import Attribute

# pylint: disable=too-few-public-methods
class PhoneNumber(Attribute):
    """phone_number"""
    def __init__(self, attr_value):
        super().__init__()
        self._error_message = "phone number is not valid"
        self._validation_pattern = r"^(\+)[0-9]{11}"
        self._attr_value = self._validate(attr_value)
