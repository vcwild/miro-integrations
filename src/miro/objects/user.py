from miro.objects.mini import MiniUserObject


class UserObject(MiniUserObject):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.created_at = data["createdAt"]
        self.company = data["company"]
        self.role = data["role"]
        self.industry = data["industry"]
        self.email = data["email"]
        self.state = data["state"]
        self.picture = data["picture"]
