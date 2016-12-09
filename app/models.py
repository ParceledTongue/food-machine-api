from app import db

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    calories = db.Column(db.Integer, index=True)
    category = db.Column(db.Integer) # enum
    unit = db.Column(db.Integer) # enum

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'calories': self.calories,
            'category': self.category,
            'unit': self.unit
        }

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1000))
    category = db.Column(db.Integer) # enum
    dish_type = db.Column(db.Integer) # enum
    prep_time = db.Column(db.Integer) # in minutes
    date_added = db.Column(db.DateTime)
    servings = db.Column(db.Integer)
    calories = db.Column(db.Integer) # per serving
    ingredients = db.relationship("Recipe_Ingredient")

    def __repr__(self):
        return '<Recipe {0}>'.format(self.name)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'dishType': self.dish_type,
            'prepTime': self.prep_time,
            'dateAdded': self.date_added,
            'numServings': self.servings,
            'caloriesPerServing': self.calories,
            'ingredientList': [i.as_dict() for i in self.ingredients]
        }

class Recipe_Ingredient(db.Model):
    __tablename__ = 'recipe_ingredient'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    amount = db.Column(db.Float)
    units = db.Column(db.Integer)
    ingredient = db.relationship("Ingredient")
    
    def __repr__(self):
        return '<Recipe_Ingredient r:{0} i:{1} a:{2} u:{3}>'.format(self.recipe_id, self.ingredient_id, self.units)
    def as_dict(self):
        return {
            'Item1': self.ingredient.as_dict(),
            'Item2': self.amount,
            'Item3': self.units
        }

class Grocery_List(db.Model):
    __tablename__ = 'grocery_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    groceries = db.relationship("Grocery")

    def __repr__(self):
        return '<Grocery_List %r>' % (self.name)

class Grocery(db.Model):
    __tablename__ = 'grocery'
    grocery_list_id = db.Column(db.Integer, db.ForeignKey('grocery_list.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    units = db.Column(db.Float)
    crossed_off = db.Column(db.Boolean)
    ingredient = db.relationship("Ingredient")

    def __repr__(self):
        return '<Grocery gl:{0} i:{1} u:{2} co:{3}>'.format(self.grocery_list_id, self.ingredient_id, self.units, self.crossed_off)

class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    products = db.relationship("Price")

    def __repr__(self):
        return '<Store %r>' % (self.name)

class Price(db.Model):
    __tablename__ = 'price'
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    cost = db.Column(db.Integer) # cents per unit
    ingredient = db.relationship("Ingredient")

    def __repr__(self):
        return '<Price s:{0} i:{1} cost:{2}>'.format(self.store_id, self.ingredient_id, self.cost)
