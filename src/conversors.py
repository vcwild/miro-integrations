from typing import Dict
from datetime import datetime, timedelta


def from_system_time_to_gmt(date: datetime) -> datetime:
    """Helper function to convert system time GMT-3 into GMT+0

    Args:
            date (datetime): Datetime object in GMT-3

    Returns:
            datetime: Datetime object in GMT+0
    """
    return date + timedelta(hours=3)


def str_to_datetime(array: list, keys: list) -> Dict:
    """Transform an array of strings into a Datetime objects.

    Args:
            array (list): List of strings to converto to datetime
            keys (list): Keys to inspect

    Returns:
            Dict: Return the same array with datetime objects for keys
    """
    for key in keys:
        array[key] = datetime.strptime(array[key], "%Y-%m-%dT%H:%M:%SZ")
        array[key] = from_system_time_to_gmt(array[key])
    return array


def convert_element_values(elements: dict, keys: list) -> Dict:
    for element in elements:
        element["id"] = int(element["id"])
        element = str_to_datetime(element, keys)
    return elements
