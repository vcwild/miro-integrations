from miro.objects.abstract_classes import BaseObject, MiroObject
from miro.objects.mini import MiniUserObject


class BoardUserConnectionObject(MiroObject):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.user = MiniUserObject(data["user"])
        self.role = data["role"]
        self.created_at = data["createdAt"]
        self.modified_at = data["modifiedAt"]
        self.created_by = MiniUserObject(data["createdBy"])
        self.modified_by = MiniUserObject(data["modifiedBy"])


class FlatBoardUserConnectionObject(BaseObject):
    def __init__(self, element) -> None:
        self.type = element["user"]["type"]
        self.id = element["user"]["id"]
        self.name = element["user"]["name"]
        self.role = element["role"]
        self.modified_at = element["modifiedAt"]
        self.created_at = element["createdAt"]


"""
Classe Board
List de Elementos
Classe Element <- Lista de Elementos
"""
