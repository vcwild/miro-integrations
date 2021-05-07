from typing import Dict
from datetime import datetime, timedelta

def from_system_time_to_gmt(date) -> datetime:
	return date + timedelta(hours=3)

def str_to_datetime(array: list, keys: list) -> Dict:
	for key in keys:
		array[key] = datetime.strptime(array[key],"%Y-%m-%dT%H:%M:%SZ")
		array[key] = from_system_time_to_gmt(array[key])
	return array

def convert_element_values(elements: dict, keys: list) -> Dict:
	for element in elements:
		element['id'] = int(element['id'])
		element = str_to_datetime(element, keys)
	return elements
