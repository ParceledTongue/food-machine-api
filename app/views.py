from flask import jsonify, request
from app import app, db, models

pre='/foodmachine/api/'

###############
# INGREDIENTS #
###############

@app.route(pre + 'ingredients', methods=['GET'])
def get_ingredients():
    ingredients = [ingredient.as_dict() for ingredient in models.Ingredient.query.all()]
    return jsonify({'ingredients': ingredients})

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.get(ingredient_id).as_dict()
    return jsonify({'ingredient': ingredient})

@app.route(pre + 'ingredients', methods=['POST'])
def create_ingredient():
    ingredient = models.Ingredient(
        name = request.json['name'],
        calories = request.json['calories'],
        category = request.json.get('category', 0),
        unit = request.json.get('unit', 0)
    )
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({'ingredient': ingredient.as_dict()})

# @app.route(pre + 'ingredients/<int:ingredient_id>', methods=['PUT'])
# def update_ingredient(ingredient_id):
# TODO

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.filter_by(id=ingredient_id);
    ingredient_dict = ingredient.as_dict()
    ingredient.delete()
    db.session.commit()
    return jsonify({'ingredient': ingredient_dict})

###########
# RECIPES #
###########

@app.route(pre + 'recipes', methods=['GET'])
def get_recipes():
    recipes = [recipe.as_dict() for recipe in models.Recipe.query.all()]
    return jsonify({'recipes': recipes})

@app.route(pre + 'recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = models.Recipe.query.get(recipe_id).as_dict()
    return jsonify({'recipe': recipe})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
