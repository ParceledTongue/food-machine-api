from flask import jsonify
from app import app, models

pre='/foodmachine/api/'

@app.route(pre + 'ingredients', methods=['GET'])
def get_ingredients():
    # TODO
    return;

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.get(ingredient_id).as_dict()
    return jsonify({'ingredient': ingredient})

@app.route(pre + 'recipes', methods=['GET'])
def get_recipes():
    # TODO
    return;

@app.route(pre + 'recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = models.Recipe.query.get(recipe_id).as_dict()
    return jsonify({'recipe': recipe})
