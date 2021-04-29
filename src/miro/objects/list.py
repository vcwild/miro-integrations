from miro.objects.abstract_classes import BaseObject
from miro.objects.board import BoardObject
from miro.objects.board_user_connection import BoardUserConnectionObject
from miro.objects.team_user_connection_object import TeamUserConnectionObject


class ListObject(BaseObject):
	def __init__(self, data) -> None:
		self.type = data['type']
		self.limit = data['limit']
		self.offset = data['offset']
		self.size = data['size']
		self._parse_data_by_data_type(data)
		try:
			self.next_link = data['nextLink']
			self.prev_link = data['prevLink']
		except:
			pass

	def _parse_data_by_data_type(self, data):
		if data['data'][0]['type'] == "board-user-connection":
			self.data = [BoardUserConnectionObject(user) for user in data['data']]
		if data['data'][0]['type'] == "team-user-connection":
			self.data = [TeamUserConnectionObject(user) for user in data['data']]
		if data['data'][0]['type'] == "board":
			self.data = [BoardObject(user) for user in data['data']]
