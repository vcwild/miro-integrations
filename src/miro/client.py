from typing import Dict
import httpx
from miro.helpers import handle_json
from miro.objects.board import BoardObject
from miro.objects.board_user_connection import BoardUserConnectionObject
from miro.objects.list import ListObject


class Client:
	def __init__(self, base_url: str, auth_token: str) -> None:
		self.base_url = base_url
		self._auth_token = auth_token
		self.auth_header = {
			'Authorization': f'Bearer {self._auth_token}'
		}

	def get_board(self, board_id: str) -> Dict:
		url = f'{self.base_url}/v1/boards/{board_id}'
		response = httpx.get(url, headers=self.auth_header)
		data = handle_json(response)
		return BoardObject(data)

	def get_board_members(self, board_id: str) -> Dict:
		url = f'{self.base_url}/v1/boards/{board_id}/user-connections'
		response = httpx.get(url, headers=self.auth_header)
		data = handle_json(response)
		return ListObject(data)

	def get_board_user_connection(self, user_id: str) -> Dict:
		url = f'{self.base_url}/v1/board-user-connections/{user_id}'
		response = httpx.get(url, headers=self.auth_header)
		data = handle_json(response)
		return BoardUserConnectionObject(data)

	def get_widgets(self, board_id: str) -> Dict:
		url = f'{self.base_url}/v1/boards/{board_id}/widgets'
		response = httpx.get(url, headers=self.auth_header)
		return handle_json(response)

	def get_logs(self,
		start_date="2019-02-02T05:34:08.000Z",
		end_date="2021-02-02T05:34:08.000Z",
		limit="10",
		offset="0") -> Dict:
		url = f'{self.base_url}/v1/audit/logs'
		querystring = {
			"createdAfter": start_date,
			"createdBefore": end_date,
			"limit": limit,
			"offset": offset
		}
		response = httpx.get(
			url,
			params=querystring,
			headers=self.auth_header
		)
		return handle_json(response)
	
	def get_team(self, team_id) -> Dict:
		url = f'https://api.miro.com/v1/teams/{team_id}/'
		response = httpx.get(url, headers=self.auth_header)
		return handle_json(response)

	def get_team_boards(self, team_id) -> Dict:
		url = f'https://api.miro.com/v1/teams/{team_id}/boards'
		response = httpx.get(url, headers=self.auth_header)
		return handle_json(response)
	
	def get_user(self, user_id) -> Dict:
		url = f'https://api.miro.com/v1/users/{user_id}'
		response = httpx.get(url, headers=self.auth_header)
		return handle_json(response)
	
	def list_all_team_members(self, team_id):
		url = f'https://api.miro.com/v1/teams/{team_id}/user-connections'
		response = httpx.get(url, headers=self.auth_header)
		data = handle_json(response)
		return ListObject(data)
