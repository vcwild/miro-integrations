import re

def filter_keys(array, keys):
	return {key: array[key] for key in array.keys() if key in keys}

def filter_html(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext
