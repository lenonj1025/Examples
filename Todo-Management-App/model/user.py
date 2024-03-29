class User:
    def __init__(self, id, username, mobile_phone, active):
        self.id = id
        self.active = active
        self.username = username
        self.mobile_phone = mobile_phone

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "mobile_phone": self.mobile_phone,
            "active": self.active
        }
