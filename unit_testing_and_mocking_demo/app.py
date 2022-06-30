def a():
    return b() + 100    # Function a depends on function b

def b():
    return 10000

class UserDao:
    def get_all_users(self):
        return [{"username": "bachy21", "age": 24}, {"username": "jane_doe", "age": 30}]

def c():
    user_dao = UserDao()
    return user_dao.get_all_users()
