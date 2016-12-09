import datetime
from flask import abort, jsonify, make_response, request, url_for
from app import app, db, models

pre='/'

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

@app.route(pre + 'ingredients/<ingredient_name>', methods=['GET'])
def get_ingredient_by_name(ingredient_name):
    ingredient = models.Ingredient.query.filter_by(name = ingredient_name).first()
    if ingredient == None:
        abort(404)
    return jsonify({'ingredient': make_public_ingredient(ingredient.as_dict())})

@app.route(pre + 'ingredients', methods=['POST'])
def create_ingredient():
    if not request.json or not 'name' in request.json:
        abort(400)
    ingredient = models.Ingredient(
        name = request.json['name'],
        calories = request.json.get('calories', -1),
        category = request.json.get('category', 0),
        unit = request.json.get('unit', 0)
    )
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({'ingredient': make_public_ingredient(ingredient.as_dict())})

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.get(ingredient_id)
    if ingredient == None:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not unicode:
        abort(400)
    if 'calories' in request.json and type(request.json['calories']) is not int:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not int:
        abort(400)
    if 'unit' in request.json and type(request.json['unit']) is not int:
        abort(400)
    ingredient.name = request.json.get('name', ingredient.name)
    ingredient.calories = request.json.get('calories', ingredient.calories)
    ingredient.category = request.json.get('category', ingredient.category)
    ingredient.unit = request.json.get('unit', ingredient.unit)
    db.session.commit()
    return jsonify({'ingredient': make_public_ingredient(ingredient.as_dict())})

@app.route(pre + 'ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    ingredient = models.Ingredient.query.get(ingredient_id)
    if ingredient == None:
        abort(404)
    ingredient_dict = ingredient.as_dict()
    db.session.delete(ingredient)
    db.session.commit()
    return jsonify({'ingredient': make_public_ingredient(ingredient_dict)})

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
    recipes = [make_public_recipe(recipe.as_dict()) for recipe in models.Recipe.query.all()]
    return jsonify({'recipes': recipes})

@app.route(pre + 'recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = models.Recipe.query.get(recipe_id)
    return jsonify({'recipe': make_public_receipe(recipe.as_dict())})

@app.route(pre + 'recipes/<recipe_name>', methods=['GET'])
def get_recipe_by_name(recipe_name):
    recipe = models.Recipe.query.filter_by(name = recipe_name).first()
    if recipe == None:
        abort(404)
    return jsonify({'recipe': make_public_recipe(recipe.as_dict())})

@app.route(pre + 'recipes', methods=['POST'])
def create_recipe():
    if not request.json or not 'name' in request.json:
        abort(400)
    recipe = models.Recipe(
        name = request.json['name'],
        description = request.json.get('description', ''),
        category = request.json.get('category', 0),
        dish_type = request.json.get('dishType', 0),
        prep_time = request.json.get('prepTime', 0),
        date_added = datetime.datetime.now(),
        servings = request.json.get('numServings', 0),
        calories = request.json.get('caloriesPerServing', -1)
    )
    db.session.add(recipe)
    db.session.commit()
    db.session.refresh(recipe)
    # add ingredients
    for ingredientEntry in request.json['ingredientList']:
        ingredient = models.Ingredient.query.filter_by(name = ingredientEntry['Item1']['name']).first()
        if ingredient == None:
            db.session.delete(recipe)
            db.session.commit()
            abort(400) # ingredient name does not exist in db
        entry = models.Recipe_Ingredient(
            recipe_id = recipe.id,
            ingredient_id = ingredient.id,
            amount = ingredientEntry['Item2'],
            units = ingredientEntry['Item3']
        )
        db.session.add(entry)
    db.session.commit()
    return jsonify({'recipe': make_public_recipe(recipe.as_dict())})

@app.route(pre + 'recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = models.Recipe.query.get(recipe_id)
    if recipe == None:
        abort(404)
    recipe_dict = recipe.as_dict()
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'recipe': make_public_recipe(recipe_dict)})

def make_public_recipe(recipe):
    new_recipe = {}
    for field in recipe:
        if field == 'id':
            new_recipe['uri'] = url_for('get_recipe', recipe_id=recipe['id'], _external=True)
        else:
            new_recipe[field] = recipe[field]
    return new_recipe

#########
# OTHER #
#########

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
