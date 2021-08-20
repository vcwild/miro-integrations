from abc import ABC


class BaseObject(ABC):
    def __str__(self):
        rep = "{}(...)"
        return rep.format(str(self.__class__).split("'")[1].split(".")[-1])

    def __repr__(self) -> str:
        rep = "{}({})"
        return rep.format(
            str(self.__class__).split("'")[1].split(".")[-1], self.__dict__
        )


class MiroObject(BaseObject, ABC):
    def __init__(self, data) -> None:
        self.type = data["type"]
        self.id = data["id"]


# class WidgetObject(MiroObject, ABC):
# 	def __init__(self, data) -> None:
# 		super().__init__(data)
# 		self.capabilities = Capabilities(data['capabilities'])
# 		self.created_at = data['createdAt']
# 		# self.metadata = ApplicationMetadata(data['metadata'])
# 		self.modified_at = data['modifiedAt']
# 		self.created_by = MiniUserObject(data['createdBy'])
# 		self.modified_by = MiniUserObject(data['modifiedBy'])
