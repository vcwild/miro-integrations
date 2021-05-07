from typing import List
from miro.objects.abstract_classes import BaseObject
from miro.objects.board import BoardObject
from miro.objects.board_user_connection import (
	BoardUserConnectionObject,
	FlatBoardUserConnectionObject
)
from miro.objects.team_user_connection_object import TeamUserConnectionObject


class ListObject(BaseObject):
	def __init__(self, data, flat=False) -> None:
		_flat = flat
		self.type = data['type']
		self.limit = data['limit']
		self.offset = data['offset']
		self.size = data['size']
		self.next_link = data['nextLink']
		self.prev_link = data['prevLink']
		self._parse_data_by_data_type(data, _flat)

	def _parse_data_by_data_type(self, data, flat) -> None:
		data_type = data['data'][0]['type']
		if flat:
			if data_type == "board-user-connection":
				self.data = [
					FlatBoardUserConnectionObject(user) for user in data['data']
				]
			return None

		if data_type == "board-user-connection":
			self.data = [
				BoardUserConnectionObject(user) for user in data['data']
			]
		if data_type == "team-user-connection":
			self.data = [
				TeamUserConnectionObject(user) for user in data['data']
			]
		if data_type == "board":
			self.data = [
				BoardObject(user) for user in data['data']
			]
