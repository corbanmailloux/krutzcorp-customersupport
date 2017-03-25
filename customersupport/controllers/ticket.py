from flask import jsonify

from customersupport import app
from customersupport.wrappers import sales


@app.route('/sales/refund/real')
def refund_order(mock=False):
    return jsonify(sales.initiate_refund(
        replace=True,
        order_id=1,
        serial_numbers=[
            123,
            456,
            789
        ],
        mock=mock).serialize())


@app.route('/sales/refund/stub')
def refund_order_stubbed():
    return refund_order(mock=True)