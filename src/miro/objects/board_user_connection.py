from miro.objects.abstract_classes import MiroObject
from miro.objects.mini import MiniUserObject


class BoardUserConnectionObject(MiroObject):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.user = MiniUserObject(data['user'])
		self.role = data['role']
		self.created_at = data['createdAt']
		self.modified_at = data['modifiedAt']
		self.created_by = MiniUserObject(data['createdBy'])
		self.modified_by = MiniUserObject(data['modifiedBy'])
