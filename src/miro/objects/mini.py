from typing import Dict
from miro.objects.abstract_classes import MiroObject


class MiniUserObject(MiroObject, Dict):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.name = data['name']


class MiniUserConnectionObject(MiroObject):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.role = data['role']
		self.user = MiniUserObject(data['user'])


class MiniTeamObject(MiroObject):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.name = data['name']


class MiniPictureObject(MiroObject):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.image_url = data['imageUrl']
