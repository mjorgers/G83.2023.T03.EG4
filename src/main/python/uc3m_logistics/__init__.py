"""UC3M Care MODULE WITH ALL THE FEATURES REQUIRED FOR ACCESS CONTROL"""

from uc3m_logistics.exception.order_management_exception import OrderManagementException
from uc3m_logistics.data.order_shipping import OrderShipping
from uc3m_logistics.config.order_manager_config import JSON_FILES_PATH
from uc3m_logistics.config.order_manager_config import JSON_FILES_RF2_PATH
from .order_manager import OrderManager
