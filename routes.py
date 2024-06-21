from flask import Flask, render_template, request, redirect, url_for, jsonify
from app import app
from models import Markets, Reviews, Cities, States, db


@app.route('/', methods=['GET'])
def page_get_index():
    sort = request.args.get('sort', 'asc', type=str)
    if sort == "desc":
        sort = "asc"
    else:
        sort = "desc"
    city = request.args.get('city', '', type=str)
    state = request.args.get('state', '', type=str)
    zipcode = request.args.get('zipcode', '', type=str)
    distance = request.args.get('distance', '', type=str)

    query = Markets.query

    if city or state or zipcode or distance:
        if city:
            current_city = Cities.query.filter_by(city=city).first()
            query = query.filter_by(city=str(current_city.city_id))
        if state:
            current_states = States.query.filter_by(state_full=state).first()
            query = query.filter_by(state=str(current_states.state_id))
        if zipcode:
            query = query.filter_by(zip=zipcode)
        if distance:
            pass

    query = query.outerjoin(Reviews).group_by(Markets.market_id).order_by(
        db.func.avg(Reviews.rating).desc() if sort == 'desc' else db.func.avg(Reviews.rating).asc())

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    markets = query.paginate(page=page, per_page=per_page)

    return render_template('index.html', markets=markets, city=city, state=state, zipcode=zipcode, distance=distance,
                           sort=sort)


@app.route('/states', methods=['GET'])
def page_get_states():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    states = States.query.paginate(page=page, per_page=per_page)

    return render_template('states.html', states=states)


@app.route('/cities', methods=['GET'])
def page_get_cities():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    cities = Cities.query.paginate(page=page, per_page=per_page)

    return render_template('cities.html', cities=cities)


@app.route('/cities/city', methods=['GET'])
def page_get_city_details():
    city_id = request.args.get('city_id', 1, type=int)
    city = Cities.query.filter_by(city_id=city_id).first()
    return render_template('city.html', city=city)


@app.route('/markets')
def page_get_markets():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    markets = Markets.query.paginate(page=page, per_page=per_page)

    return render_template('markets.html', markets=markets)


@app.route('/markets/market', methods=['GET'])
def page_get_market_details():
    market_id = request.args.get('market_id', 1, type=int)
    market = Markets.query.filter_by(market_id=market_id).first()
    delete_review_id = request.args.get('delete_review_id', -1, type=int)
    if (delete_review_id > 0):
        review = Reviews.query.filter_by(review_id=delete_review_id).first()
        db.session.delete(review)
        db.session.commit()

    return render_template('market.html', market=market)


@app.route('/markets/market', methods=['POST'])
def post_reviews():
    market_id = request.args.get('market_id', 1, type=int)
    user_name = request.form.get('user_name', '', type=str)
    text = request.form.get('text', '', type=str)
    rating = request.form.get('rating', 0, type=int)
    market = Markets.query.filter_by(market_id=market_id).first()
    review = Reviews(
        market_id=market_id,
        user_name=user_name,
        rating=rating,
        text=text
    )

    db.session.add(review)
    db.session.commit()

    return render_template('market.html', market=market, user_name=user_name, text=text, rating=rating)
