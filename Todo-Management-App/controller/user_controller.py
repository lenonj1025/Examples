from flask import Blueprint, request
from model.user import User
from service.user_service import UserService
from exception.invalid_parameter import InvalidParameterError
from exception.user_not_found import UserNotFoundError

uc = Blueprint('user_controller', __name__)
user_service = UserService()

@uc.route('/users')
def get_all_users():
    return{
        "users": user_service.get_all_users()   # a list of dictionaries
    }


@uc.route('/users/<user_id>')
def get_user_by_id(user_id):
    try:
        return user_service.get_user_by_id(user_id)
    except UserNotFoundError as e:
        return {
                   "message": str(e)
               }, 404

@uc.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        user_service.delete_user_by_id(user_id)

        return {
            "message": f"User with id {user_id} deleted successfully"
        }
    except UserNotFoundError as e:
        return {
            "message": str(e)
        }, 404

@uc.route('/users/<user_id>', methods=['POST'])
def update_user_by_id(user_id):
    try:
        json_dictionary = request.get_json()
        return user_service.update_user_by_id(User(user_id,
                                                   json_dictionary['username'], json_dictionary['mobile_phone'],
                                                   json_dictionary['active']))
    except UserNotFoundError as e:
        return{
            "message": str(e)
        }, 404

@uc.route('/users', methods=['POST'])
def add_user():
    user_json_dictionary = request.get_json()
    user_object = User(None, user_json_dictionary['username'], user_json_dictionary['mobile_phone'], None)
    try:
        return user_service.add_user(user_object), 201
    except InvalidParameterError as e:
        return{
            "message": str(e)
        }, 400
