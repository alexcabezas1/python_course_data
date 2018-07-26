from __future__ import absolute_import, division, print_function, unicode_literals

import testdata
from collections import namedtuple
import sys
import csv
import random

Item = namedtuple('Item', ['name','quantity','unit','unit_price','category'])

ITEMS = [
    Item('Blueberries',1,'pint',3.99,'fruits-vegetables'),
    Item('Cucumber',1,'medium',0.50,'fruits-vegetables'),
    Item('Organic Baby Carrots',1,'lb',1.69,'fruits-vegetables'),
    Item('Organic Greenhouse Grape Tomatoes',1,'pint',4.99,'fruits-vegetables'),
    Item('Yellow Onion',1,'large',1.24,'fruits-vegetables'),
    Item('Broccoli',1,'bunch',2.29,'fruits-vegetables'),
    Item('Garlic',1,'bulb',0.50,'fruits-vegetables'),
    Item('Red Bell Pepper',1,'medium',1.49,'fruits-vegetables'),
    Item('Cilantro',1,'bunch',1.35,'fruits-vegetables'),
    Item('Green Bell Pepper',1,'medium',0.78,'fruits-vegetables'),
    Item('Red Raspberries',6,'oz',2.99,'fruits-vegetables'),
    Item('Brussels Sprouts',1,'lb',2.99,'fruits-vegetables'),
    Item('Lime',1,'medium',2.99,'fruits-vegetables'),
    Item('Hass Avocado',1,'large',1.29,'fruits-vegetables'),
    Item('Mandarin Oranges',3,'lb',7.99,'fruits-vegetables'),
    Item('Red Apple',1,'medium',1.20,'fruits-vegetables'),
    Item('Green Seedless Grapes',2,'lb',5.98,'fruits-vegetables'),
    Item('Organic Roma Tomatoes',1,'lb',2.49,'fruits-vegetables'),
    Item('Organic Carrots',2,'lb',1.99,'fruits-vegetables'),
    Item('Ginger',8,'oz',1.50,'fruits-vegetables'),
    Item('Iceberg Lettuce',1,'head',0.99,'fruits-vegetables'),
    Item('Cauliflower',1,'head',3.99,'fruits-vegetables'),
    Item('Fresh Atlantic Salmon',12,'oz',6.74,'seafood'),
    Item('Lean Ground Turkey',16,'oz',3.99,'meat'),
    Item('Hand-Trimmed Boneless, Skinless Chicken',2,'lb',11.02,'meat'),
    Item('Beef Stew Meat',1,'lb',6.99,'meat'),
    Item('Boneless Center Cut Pork Chops',1,'lb',6.99,'meat'),
    Item('Choice Beef Chuck Roast',2,'lb',13.98,'meat'),
    Item('Lean Ground Beef',1,'lb',6.99,'meat'),
    Item('Crispy Tenders',9,'oz',4.49,'meat'),
    Item('Choice Flat Iron Steak',8,'oz',5.00,'meat'),
    Item('Original Breakfast Sausage Links',12,'oz',3.69,'meat')
]

class Transaction(testdata.DictFactory):
    id = testdata.CountingFactory(1518144480)
    account = testdata.RandomSelection(['anyuser@gmail.com'])
    item = testdata.RandomSelection(ITEMS)
    quantity = testdata.RandomInteger(1,3)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise SystemExit('Usage: generator.py csv|txt items_numbers')
    
    output_type = sys.argv[1]
    items_numbers = int(sys.argv[2]) # 50
    
    header = ['id','account','purchased_quantity','item_name','item_quantity','item_unit','item_price','category']

    if sys.argv[1] == "csv":
        with open('ecommerce_transactions.csv', 'wb') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(header)
            for t in Transaction().generate(items_numbers):
                writer.writerow([t['id'],
                                t['account'],
                                t['quantity'],
                                t['item'].name,
                                t['item'].quantity,
                                t['item'].unit,
                                t['item'].unit_price,
                                t['item'].category])
    
    if sys.argv[1] == "txt":
        with open('ecommerce_transactions.txt','wb') as f:
            header = ['"{}"'.format(v) for v in header]
            print(",".join(header), file=f)
            for t in Transaction().generate(items_numbers):
                values = [t['id'],
                         t['account'],
                         t['quantity'],
                         t['item'].name,
                         t['item'].quantity,
                         t['item'].unit,
                         t['item'].unit_price,
                         t['item'].category]
                values = map(lambda v: '"{}"'.format(v.replace(",","")) if isinstance(v, unicode) else str(v), values)
                
                print(",".join(values), file=f)

    
    if sys.argv[1] == "random_prices":
        with open('prices_another_store.csv', 'wb') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(['item_name', 'item_price'])
            for t in ITEMS:
                new_price = float("{:.2f}".format(random.uniform(0.5, 4.5)))
                writer.writerow([t.name,
                                 new_price])
            