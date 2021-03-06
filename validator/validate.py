from jsonschema import validate
from html5_parser import parse
import re
import json
import glob
import sys


def jr(f):
    with open(f, 'r') as file:
        return json.loads(file.read())


def v(name, j, schema):
    try:
        validate(j, schema)
    except:
        print(f"Error validating: {name}")
        sys.exit(1)

def verify_html(txt, name):
    try:
        parse(txt)
    except:
        print(f"Error validating: {name}")
        sys.exit(1)


joyride_schema = jr('joyride.schema.json')
routes_schema = jr('routes.schema.json')

products = jr('routes.json')
v('products', products, routes_schema)
for route in products['routes']:
    try:
        re.compile(route['url'])
    except:
        print(f"Error validating route: {route['url']}")
        sys.exit(1)

for j in glob.glob('*/*.json'):
    print(f'Checking {j}')
    data = jr(j)
    v(j, data, joyride_schema)

    for step in data['steps']:
        for key in step['content']:
            verify_html(step['content'][key], j)
        for key in step['title']:
            verify_html(step['title'][key], j)

sys.exit(0)
