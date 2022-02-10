from raw_data import users, orders, offers


def user_dict(data):
    return {
        "id": data.id,
        "first_name": data.first_name,
        "last_name": data.last_name,
        "age": data.age,
        "email": data.email,
        "role": data.role,
        "phone": data.phone,
    }


def order_dict(data):
    return {
        "id": data.id,
        "name": data.name,
        "description": data.description,
        "start_date": data.start_date,
        "end_date": data.end_date,
        "address": data.address,
        "price": data.price,
        "customer_id": data.customer_id,
        "executor_id": data.executor_id,
    }


def offer_dict(data):
    return {
        "id": data.id,
        "order_id": data.order_id,
        "executor_id": data.executor_id,
    }


def template_integrate_keys_into_table(data, name: str):
    """
    :param data: users
    :param name: "user"
    :return: "id": user.id,
    """
    keys = data[0].keys()
    for key in keys:
        print(f'"{key}": {name}.{key},')


# template_integrate_keys_into_table(users, "user")
# template_integrate_keys_into_table(orders, "order")
# template_integrate_keys_into_table(offers, "offer")


def template_integrate_keys_with_value_into_table(data, single_data):
    """
    :param data: users
    :param single_data: "user"
    :return: id=user["id"],
    """
    keys = data[0].keys()
    for key in keys:
        print(f'{key}={single_data}["{key}"],')


# template_integrate_keys_with_value_into_table(users, "user")
# template_integrate_keys_with_value_into_table(orders, "order")
# template_integrate_keys_with_value_into_table(offers, "offer")
