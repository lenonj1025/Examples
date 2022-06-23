from flask import Flask
from controller.user_controller import uc
if __name__ == '__main__':
    app = Flask(__name__)

    app.register_Blueprint(uc)

    app.run(port=8080, debug=True)
