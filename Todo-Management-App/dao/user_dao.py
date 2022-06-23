from model.user import User
# Right now, we don't have a database to connect to
# So we will store data inside a collection
users = {
    "bach21": User("bach21", "512-826-0001"),
    "jane12345": User("jane12345", "512-826-0002")
}

class UserDao:

    # Crud Operations
    # Create - insert a new user into our "database"
    # Read - Retrieve a user or users form our "database
    # Update - Update a user in out "database"
    # Delete - Delete a user in our "database"
    def get_user_by_username(self, username):
        return users[username]  # Returns a user object

    def get_all_users(self):
        users_values = []
        for value in users.values():
            users_values.append(value)

        return users_values # Returns a list of user objects

    def add_user(self, user):   # User will represent a User Object
        users[user['username']] = user

        return user

    def edit_user_by_username(self, username, new_user_info): # new_user_info will be a User object
        if username == new_user_info.username:    # if we are not updated the username, replace the rest of the info
            users[username] = new_user_info
        else:   # Otherwise, delete the original key-value pair and create new key-value pair
            del users[username]
            users[new_user_info.username] = new_user_info

        return new_user_info
