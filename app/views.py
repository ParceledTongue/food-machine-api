from flask import abort, jsonify, make_response, request, url_for
from app import app, db, models

pre='/foodmachine/api/'

###############
# INGREDIENTS #
###############

@app.route(pre + 'ingredients', methods=['GET'])
def get_ingredients():
    ingredients = [make_public_ingredient(ingredient.as_dict()) for ingredient in models.Ingredient.query.all()]
    return jsonify({'ingredients': ingredients})

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.get(ingredient_id)
    if ingredient == None:
        abort(404)
    return jsonify({'ingredient': make_public_ingredient(ingredient.as_dict())})

@app.route(pre + 'ingredients', methods=['POST'])
def create_ingredient():
    if not request.json or not 'title' in request.json:
        abort(400)
    ingredient = models.Ingredient(
        name = request.json['name'],
        calories = request.json['calories'],
        category = request.json.get('category', 0),
        unit = request.json.get('unit', 0)
    )
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({'ingredient': make_public_ingredient(ingredient.as_dict())})

#@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['PUT'])
#def update_ingredient(ingredient_id):
#    ingredient = models.Ingredient.query.get(ingredient_id)
#    if ingredient == None:
#        abort(404)
#    if not request.json:
#        abort(400)
#    if 'name' in request.json and type(request.json['name']) is not unicode:
#        abort(400)
#    if 'calories' in request.json and type(request.json['calories']) is not int:
#        abort(400)
#    if 'category' in request.json and type(request.json['category']) is not int:
#        abort(400)
#    if 'unit' in request.json and type(request.json['unit']) is not int:
#        abort(400)

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.filter_by(id=ingredient_id);
    ingredient_dict = ingredient.as_dict()
    ingredient.delete()
    db.session.commit()
    return jsonify({'ingredient': ingredient_dict})

def make_public_ingredient(ingredient):
    new_ingredient = {}
    for field in ingredient:
        if field == 'id':
            new_ingredient['uri'] = url_for('get_ingredient', ingredient_id=ingredient['id'], _external=True)
        else:
            new_ingredient[field] = ingredient[field]
    return new_ingredient


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

#########
# OTHER #
#########

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
