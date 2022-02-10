from setup_db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String)
    phone = db.Column(db.String(20))

    offer_id = db.Column(db.Integer, db.ForeignKey("offer.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))

    offer = db.relationship("Offer", foreign_keys=[offer_id])
    order = db.relationship("Order", foreign_keys=[order_id])


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String)
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    address = db.Column(db.String)
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])


class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    order = db.relationship("Order", foreign_keys=[order_id])
    user = db.relationship("User", foreign_keys=[executor_id])

