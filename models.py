from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password_hash = db.Column(db.String)
    fname = db.Column(db.String, nullable=True)
    lname = db.Column(db.String, nullable=True)


class Categories(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))


class Markets(db.Model):
    __tablename__ = 'markets'
    market_id = db.Column(db.Integer, primary_key=True)
    market_name = db.Column(db.String(100))
    street = db.Column(db.String(100))
    city = db.Column(db.String, db.ForeignKey('cities.city_id'))
    state = db.Column(db.String, db.ForeignKey('states.state_id'))
    zip = db.Column(db.String(10))
    lat = db.Column(db.String)
    lon = db.Column(db.String)
    city_info = db.relationship('Cities', backref=db.backref('markets', lazy=True))
    state_info = db.relationship('States', backref=db.backref('markets', lazy=True))

    def reviews(self):
        reviews = Reviews.query.filter_by(market_id=self.market_id).all()
        return reviews

    def rating(self):
        rating_val = 0
        rating_count = 0
        reviews = Reviews.query.filter_by(market_id=self.market_id).all()
        for review in reviews:
            rating_val += review.rating
            rating_count += 1
        if rating_count > 0:
            return rating_val / rating_count
        return ''


class MarketsCategories(db.Model):
    __tablename__ = 'markets_categories'
    market_category_id = db.Column(db.Integer, primary_key=True)
    market_id = db.Column(db.Integer, db.ForeignKey('market.market_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))


class States(db.Model):
    __tablename__ = 'states'
    state_id = db.Column(db.Integer, primary_key=True)
    state_full = db.Column(db.String(100))
    state_abbr = db.Column(db.String(10))


class Cities(db.Model):
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    state_id = db.Column(db.Integer, db.ForeignKey('states.state_id'))
    state = db.relationship('States', backref=db.backref('cities', lazy=True))


class Reviews(db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    market_id = db.Column(db.Integer, db.ForeignKey('markets.market_id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user_name = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer)
    text = db.Column(db.Text, nullable=True)
    market = db.relationship('Markets', backref=db.backref('reviews', lazy=True))
