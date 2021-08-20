from miro.objects.abstract_classes import MiroObject
from miro.objects.mini import MiniUserObject, MiniTeamObject


class AuthorizationObject(MiroObject):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.created_at = data["created_at"]
        self.created_by = MiniUserObject(data["created_by"])
        self.team = MiniTeamObject(data["team"])
        self.user = MiniUserObject(data["user"])
        self.scopes = data["scopes"]
