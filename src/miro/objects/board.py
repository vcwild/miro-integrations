from miro.objects.abstract_classes import MiroObject
from miro.objects.mini import (
    MiniUserObject,
    MiniPictureObject,
    MiniUserConnectionObject,
)


class BoardObject(MiroObject):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.created_at = data["createdAt"]
        self.modified_at = data["modifiedAt"]
        self.created_by = MiniUserObject(data["createdBy"])
        self.modified_by = MiniUserObject(data["modifiedBy"])
        self.owner = MiniUserObject(data["owner"])
        self.name = data["name"]
        self.description = data["description"]
        # self.picture = MiniPictureObject(data['picture'])
        self.view_link = data["viewLink"]
        self.sharing_policy = data["sharingPolicy"]
        self.sharing_policy_access = data["sharingPolicy"]["access"]
        self.sharing_policy_team_access = data["sharingPolicy"]["teamAccess"]
        self.current_user_connection = MiniUserConnectionObject(
            data["currentUserConnection"]
        )
