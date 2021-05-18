from operator import itemgetter
from typing import List

def sort_by_key(array: list, by: str) -> List:
	sorted_array = sorted(array, key=itemgetter(by))
	return sorted_array
