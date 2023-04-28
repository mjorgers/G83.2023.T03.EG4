"""module"""
from uc3m_logistics.exception.order_management_exception import OrderManagementException
# pylint: disable=relative-beyond-top-level
from .attribute import Attribute

# pylint: disable=too-few-public-methods
class ProductId(Attribute):
    """Product_id"""

    def __init__(self, attr_value):
        super().__init__()
        self._error_message = "Invalid EAN13 code string"
        self._validation_pattern = r"^[0-9]{13}$"
        self._attr_value = self._validate(attr_value)

    def _validate(self, value):

        checksum = 0
        code_read = -1

        super()._validate(value)

        for i, digit in enumerate(reversed(value)):
            try:
                current_digit = int(digit)
            except ValueError as v_e:
                raise OrderManagementException("Invalid EAN13 code string") from v_e
            if i == 0:
                code_read = current_digit
            else:
                checksum += current_digit * 3 if (i % 2 != 0) else current_digit
        control_digit = (10 - (checksum % 10)) % 10

        if not ((code_read != -1) and (code_read == control_digit)):
            raise OrderManagementException("Invalid EAN13 control digit")
        return value
