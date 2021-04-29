from miro.objects.abstract_classes import MiroObject


class Capabilities(MiroObject):
	def __init__(self, data) -> None:
		super().__init__(data)
		self.capabilities = data['capabilities']
