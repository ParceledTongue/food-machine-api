from app import db

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    calories = db.Column(db.Integer, index=True)
    category = db.Column(db.String(20)) # should be made enum eventually
    unit = db.Column(db.String(5))

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)

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
