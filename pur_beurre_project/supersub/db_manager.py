""" DB manager module
"""
from off_api_manager import OffApiManager


class DbManager:
    """
    """
    def __init__(self):
        off_api_manager = OffApiManager()
        off_api_manager.download_products()
        self.source_data = off_api_manager.products