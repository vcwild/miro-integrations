from operator import itemgetter
from typing import Dict


def sort_by_key(array: dict, by: str) -> Dict:
    """Sort dictionary elements by given key

    Args:
            array (dict): Dictionary to be sorted
            by (str): Key to sort the dictionary

    Returns:
            Dict: Returns sorted dictionary
    """
    sorted_array = sorted(array, key=itemgetter(by))
    return sorted_array
