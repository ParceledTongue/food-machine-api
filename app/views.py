#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
api_path='/foodmachine/api/'

# very crude authentication system

@auth.get_password
def get_password(username):
    if username == 'yes':
        return 'and'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

app = Flask(__name__)

@app.route(api_path + 'ingredients', methods=['GET'])
def get_ingredients():
    # TODO

@app.route(api_path + 'ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    # TODO

@app.route(api_path + 'ingredients', methods=['POST'])
@auth.login_required
def create_ingredient():
    # TODO

@app.route(api_path + 'ingredients/<int:ingredient_id>', methods=['PUT'])
@auth.login_required
def update_ingredient(ingredient_id):
    # TODO

@app.route(api_path + 'ingredients/<int:ingredient_id>', methods=['DELETE'])
@auth.login_required
def delete_ingredient(ingredient_id):
    # TODO

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
