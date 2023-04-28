"""module"""
# pylint: disable=relative-beyond-top-level
from .attribute import Attribute

# pylint: disable=too-few-public-methods
class ZipCode(Attribute):
    """zipcode"""
    def __init__(self, attr_value):
        super().__init__()
        self._error_message = "zip_code is not valid"
        self._validation_pattern = r"^(?:0[1-9]|[1-4]\d|5[0-2])\d{3}$"  # obtenido de stackoverflow
        self._attr_value = self._validate(attr_value)
