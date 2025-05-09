from flask import Flask, render_template, request, jsonify

import logging

from service import UserService
from register_user_dto import RegisterUserDto
from response_data import ResponseData

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


user_service = UserService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users/register', methods=['POST'])
def register_user():

    register_user_data = request.get_json()
    logger.info(f"register user: {register_user_data}")
    register_user_dto = RegisterUserDto(**register_user_data)

    response_data: ResponseData = user_service.register_user(register_user_dto)

    return jsonify(invalid_field_names=response_data.get_invalid_field_names()), response_data.get_error_code()

if __name__ == '__main__':
    app.run(debug=True)