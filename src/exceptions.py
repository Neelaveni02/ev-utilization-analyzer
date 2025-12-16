"""
Custom exceptions for the EV Charging Station Utilization Analyzer.
"""

class DataSourceError(Exception):
    """Raised when the data source cannot be found or read."""
    pass

class DataFormatError(Exception):
    """Raised when the dataset does not have the expected format."""
    pass
