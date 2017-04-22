from flask import jsonify
from flask import request

from customersupport import app
from customersupport.wrappers import sales
from customersupport.util import get_param_from_request_if_not_empty


def check_address(address):
    value = request.args.get(address)
    if value == 'billing':
        return True
    else:
        return False


# select which order search to use
# if order id exists use order search
# otherwise order info
@app.route('/api/order/search')
def select_search():
    orders = sales.get_orders(
        address=get_param_from_request_if_not_empty('street_address'),
        billing_address=check_address('address'),  # check if radio button click,
        city=get_param_from_request_if_not_empty('city'),
        state=get_param_from_request_if_not_empty('state'),
        zipcode=get_param_from_request_if_not_empty('zipcode'),
        first_name=get_param_from_request_if_not_empty('first_name'),
        last_name=get_param_from_request_if_not_empty('last_name'),
        customer_id=get_param_from_request_if_not_empty('customer'),
        mock=False
    )

    # Call the Sales API to get matching . Used by the search-order

    if orders is not None:
        return jsonify([c.serialize() for c in orders])


@app.route('/api/orderid/search')
def search_order_id():

    orders = sales.get_order_info(
        order_id=get_param_from_request_if_not_empty('order_id'),
        mock=False
    )

    if orders is not None:
        return jsonify([c.serialize() for c in orders])


@app.route('/api/orderitem')
def get_info():
    order_id = get_param_from_request_if_not_empty('order_id')
    if order_id is not None:
        order_info = sales.get_order_info(
            order_id=order_id, mock=False
        )
        order = order_info
        items_list = order.items
        return jsonify([c.serialize() for c in items_list])
    return jsonify([])
