'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


max_order_value = 10_000
max_payment_value = 100_000

def validorder(order: Order):
    total_charged=0
    total_paid=0
    net = 0

    for item in order.items:
        print(item)
        if item.type == 'payment':
            if ((item.amount >=(max_payment_value*-1)) & (item.amount <= max_payment_value)):
                total_paid += Decimal(str(item.amount))
        elif item.type == 'product':
            product_total = Decimal(str(item.amount)) *  Decimal(str(item.quantity))
            print(f"product_total:{product_total}")
            total_charged += product_total
        else:
            return "Invalid item type: %s" % item.type
        print(f"{order.id} : net {net}")
    net = total_paid-total_charged

    if ( (max_order_value *-1)  > total_paid) | (total_paid > (max_order_value )):
        return 'Total amount payable for an order exceeded'

    print(f"total = {net}")
    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    if ( (max_order_value *-1)  > net) | (net > (max_order_value )):
        return 'Total amount payable for an order exceeded'
    else:
        return "Order ID: %s - Full payment received!" % order.id
    