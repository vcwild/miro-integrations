from collections import Counter
from itertools import groupby
from datetime import datetime, timedelta
from typing import Dict
from conversors import (
	from_system_time_to_gmt,
	str_to_datetime
)
from filters import remove_html, filter_keys, filter_links
from miro.client import Client

def get_user_activity_by_widget_type(
	client: Client,
	board_id: str,
	from_minutes: int,
	type: str='sticker'):
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

def get_user_data_with_text_fields(client: Client, board_id: str, from_minutes: int) -> Dict:
	board = client.list_all_widgets(board_id)

	types = ['text', 'sticker']

	board_data = []
	for item in board['data']:
		if item['type'] in types:
			item_with_datetime = str_to_datetime(item, ['modifiedAt'])

			filtered_dict = filter_keys(
				item_with_datetime,
				['modifiedAt', 'modifiedBy', 'text']
			)
			filtered_dict['text'] = remove_html(filtered_dict['text'])
			filtered_dict['user'] = filtered_dict['modifiedBy']['name']
			filtered_dict['user_id'] = filtered_dict['modifiedBy']['id']

			filtered_dict.pop('modifiedBy')
			board_data.append(filtered_dict)

	time_gmt_minus_n_minutes = \
		from_system_time_to_gmt(datetime.now()) - timedelta(minutes=from_minutes)

	board_data = list(filter(
		lambda x: x['modifiedAt'] >= time_gmt_minus_n_minutes , board_data
	))

	return board_data

def get_user_data_with_links(client: Client, board_id: str, from_minutes: int) -> Dict:
	board = client.list_all_widgets(board_id)

	types = ['text', 'sticker']

	board_data = []
	for item in board['data']:
		if item['type'] in types:
			item_with_datetime = str_to_datetime(item, ['modifiedAt'])

			filtered_dict = filter_keys(
				item_with_datetime,
				['modifiedAt', 'modifiedBy', 'text']
			)
			filtered_dict['text'] = filter_links(filtered_dict['text'])
			filtered_dict['user'] = filtered_dict['modifiedBy']['name']
			filtered_dict['user_id'] = filtered_dict['modifiedBy']['id']

			filtered_dict.pop('modifiedBy')
			if filtered_dict['text']:
				board_data.append(filtered_dict)

	time_gmt_minus_n_minutes = \
		from_system_time_to_gmt(datetime.now()) - timedelta(minutes=from_minutes)

	board_data = list(filter(
		lambda x: x['modifiedAt'] >= time_gmt_minus_n_minutes , board_data
	))

	return board_data

def get_user_reports(user_activity):
	sorted_user_activity = sorted(user_activity, key=lambda x: x['modifiedAt'], reverse=False)

	grouped_data = groupby(sorted_user_activity, key=lambda x: x['user'])

	users = {}
	for key, group in grouped_data:
		users[str(key)] = list(group)

	user_reports = {}
	for user_k, user_v in users.items():
		user_text = []
		for element in user_v:
			user_text.append(element['text'])
		user_reports[str(user_k)] = user_text

	return user_reports
