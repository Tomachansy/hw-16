from flask import Flask, request, jsonify
import insert_data
from config import Config
from setup_db import db
from create_models import User, Order, Offer
from func import user_dict, order_dict, offer_dict


app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
with app.app_context():
    db.create_all()
    insert_data.create_data(db)


@app.route('/users', methods=["GET", "POST"])
def all_users():
    if request.method == "GET":
        user_response = []
        users_list = User.query.all()
        for user in users_list:
            user_response.append(user_dict(user))

        return jsonify(user_response), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "POST":
        user = request.json
        new_user = User(
            id=user["id"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            age=user["age"],
            email=user["email"],
            role=user["role"],
            phone=user["phone"],
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(user_dict(new_user)), 201, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/users/<int:id>', methods=["GET", "PUT", "DELETE"])
def user_by_id(id: int):
    if request.method == "GET":
        user = User.query.get(id)
        if user is None:
            return "User not found"

        return jsonify(user_dict(user)), 200, {'Content-Type': 'application/json; charset=utf8'}

    elif request.method == "PUT":
        user = request.json
        upd_user = User.query.get(id)
        upd_user.first_name = user["first_name"]
        upd_user.last_name = user["last_name"]
        upd_user.age = user["age"]
        upd_user.email = user["email"]
        upd_user.role = user["role"]
        upd_user.phone = user["phone"]

        db.session.add(upd_user)
        db.session.commit()

        return jsonify(""), 204

    elif request.method == "DELETE":
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify(""), 204


@app.route('/orders', methods=["GET", "POST"])
def all_orders():
    if request.method == "GET":
        order_response = []
        orders_list = Order.query.all()
        for order in orders_list:
            order_response.append(order_dict(order))

        return jsonify(order_response), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "POST":
        order = request.json
        new_order = Order(
            id=order["id"],
            name=order["name"],
            description=order["description"],
            start_date=order["start_date"],
            end_date=order["end_date"],
            address=order["address"],
            price=order["price"],
            customer_id=order["customer_id"],
            executor_id=order["executor_id"],
        )
        db.session.add(new_order)
        db.session.commit()

        return jsonify(order_dict(new_order)), 201, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/orders/<int:id>', methods=["GET", "PUT", "DELETE"])
def order_by_id(id: int):
    if request.method == "GET":
        order = Order.query.get(id)
        if order is None:
            return "Order not found"

        return jsonify(order_dict(order)), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "PUT":
        order = request.json
        upd_order = Order.query.get(id)
        upd_order.name = order["name"]
        upd_order.description = order["description"]
        upd_order.start_date = order["start_date"]
        upd_order.end_date = order["end_date"]
        upd_order.address = order["address"]
        upd_order.price = order["price"]
        upd_order.customer_id = order["customer_id"]
        upd_order.executor_id = order["executor_id"]

        db.session.add(upd_order)
        db.session.commit()

        return jsonify(""), 204

    elif request.method == "DELETE":
        order = Order.query.get(id)

        db.session.delete(order)
        db.session.commit()

        return jsonify(""), 204


@app.route('/offers', methods=["GET", "POST"])
def all_offers():
    if request.method == "GET":
        offer_response = []
        offers_list = Offer.query.all()
        for offer in offers_list:
            offer_response.append(offer_dict(offer))

        return jsonify(offer_response), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "POST":
        offer = request.json
        new_offer = Offer(
            id=offer["id"],
            order_id=offer["order_id"],
            executor_id=offer["executor_id"],
        )
        db.session.add(new_offer)
        db.session.commit()

        return jsonify(offer_dict(new_offer)), 201, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/offers/<int:id>', methods=["GET", "PUT", "DELETE"])
def offer_by_id(id: int):
    if request.method == "GET":
        offer = Offer.query.get(id)
        if offer is None:
            return "Order not found"

        return jsonify(offer_dict(offer)), 200, {'Content-Type': 'application/json; charset=utf-8'}

    elif request.method == "PUT":
        offer = request.json
        upd_offer = Offer.query.get(id)
        upd_offer.order_id = offer["order_id"]
        upd_offer.executor_id = offer["executor_id"]
        db.session.add(upd_offer)
        db.session.commit()

        return jsonify(""), 204

    elif request.method == "DELETE":
        offer = Offer.query.get(id)

        db.session.delete(offer)
        db.session.commit()

        return jsonify(""), 204


if __name__ == '__main__':
    app.run(debug=True)
