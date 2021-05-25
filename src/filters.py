import re
from typing import Dict

def filter_keys(array: dict, keys: str) -> Dict:
	return {key: array[key] for key in array.keys() if key in keys}

def filter_html(raw_html: str) -> str:
	"""Clears html tags out

	Args:
		raw_html (str): Html string

	Returns:
		str: String without html tags
	"""
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext
