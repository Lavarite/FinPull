"""
User interface modules for FinScraper
"""

from .api import FinancialDataAPI
from .cli import FinancialDataCLI

# GUI import is conditional
try:
    from .gui import FinancialDataGUI
    __all__ = ["FinancialDataAPI", "FinancialDataCLI", "FinancialDataGUI"]
except ImportError:
    __all__ = ["FinancialDataAPI", "FinancialDataCLI"] 