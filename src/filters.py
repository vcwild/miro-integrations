def filter_keys(array, keys):
	return {key: array[key] for key in array.keys() if key in keys}
