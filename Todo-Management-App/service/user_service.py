from dao.user_dao import UserDao
from exception.invalid_parameter import InvalidParameterError

class UserService:

    def __init__(self):
        self.user_dao = UserDao()
    # Get a list of User objects from the DAO layer
    # convert the user objects into dictionaries
    # return a list of dictionaries that each represent the users

    def get_all_users(self):
        list_of_user_objects = self.user_dao.get_all_users()

        # Method #1, use a for loop and do it manually
        list_of_user_dictionaries = []
        for user_obj in list_of_user_objects:
            list_of_user_dictionaries.append(user_obj.to_dict())

        return list_of_user_dictionaries

        # Method #2, use map
        # return list(map(lambda x: x.to_dict(), list_of_user_objects))

    def get_user_by_username(self, username):
        user_obj = self.user_dao.get_user_by_username(username)
        return user_obj.to_dict()

    # 1. Check if username is at least 6 characters
    # 2. Check if username contains spaces
    # Invoke add_user in DAO, passing in a user_object
    # Return the dictionary representation of the return value from that method
    def add_user(self):
        if " " in user_object.username:
            raise InvalidParameterError("Username cannot contain spaces!")

        if len(user_object.username) < 6:
            raise InvalidParameterError("Username must be at least 6 characters")
        added_user_object = self.user_dao.add.user(user_object)
        return added_user_object.to_dict()

    # Invoke add_user in DAO, passing in a username and user_object
    # Return the dictionary representation of the return value from that method
    def edit_user_by_username(self, username):
        edited_user_obj = self.user_dao.edit_user_by_username(username, user_object)
        return edited_user_obj.to_dict()
