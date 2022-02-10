import raw_data
from create_models import User, Order, Offer


def create_data(db):
    for user in raw_data.users:
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

    for order in raw_data.orders:
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

    for offer in raw_data.offers:
        new_offer = Offer(
            id=offer["id"],
            order_id=offer["order_id"],
            executor_id=offer["executor_id"],
        )
        db.session.add(new_offer)
        db.session.commit()
