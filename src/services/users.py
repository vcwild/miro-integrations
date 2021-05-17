from collections import Counter
from datetime import datetime, timedelta
from typing import Dict
from conversors import (
	from_system_time_to_gmt,
	str_to_datetime
)
from filters import filter_keys
from miro.client import Client

def get_user_activity_by_widget_type(client: Client, board_id: str, from_minutes: int, type: str='sticker'):
	board = client.list_all_widgets(board_id)
	items = [item for item in board['data'] if item['type'] in type]

	board_data = []
	for item in items:
		item_with_datetime = str_to_datetime(item, ['modifiedAt'])
		filtered_dict = filter_keys(
			item_with_datetime,
			['modifiedAt', 'modifiedBy', 'type']
		)

		filtered_dict['user'] = filtered_dict['modifiedBy']['name']
		filtered_dict['user_id'] = filtered_dict['modifiedBy']['id']

		filtered_dict.pop('modifiedBy')
		board_data.append(filtered_dict)

	time_gmt_minus_n_minutes = \
		from_system_time_to_gmt(datetime.now()) - timedelta(minutes=from_minutes)

	board_data = list(filter(
		lambda x: x['modifiedAt'] >= time_gmt_minus_n_minutes , board_data
	))

	users = dict(Counter(item['user'] for item in board_data))

	return users

def get_user_activity(client: Client, board_id: str, from_minutes: int) -> Dict:
	board = client.list_all_widgets(board_id)
	board_data = []
	for item in board['data']:
		item_with_datetime = str_to_datetime(item, ['modifiedAt'])
		filtered_dict = filter_keys(
			item_with_datetime,
			['modifiedAt', 'modifiedBy']
		)

		filtered_dict['user'] = filtered_dict['modifiedBy']['name']
		filtered_dict['user_id'] = filtered_dict['modifiedBy']['id']

		filtered_dict.pop('modifiedBy')
		board_data.append(filtered_dict)

	time_gmt_minus_n_minutes = \
		from_system_time_to_gmt(datetime.now()) - timedelta(minutes=from_minutes)

	board_data = list(filter(
		lambda x: x['modifiedAt'] >= time_gmt_minus_n_minutes , board_data
	))

	users = dict(Counter(item['user'] for item in board_data))

	return users

