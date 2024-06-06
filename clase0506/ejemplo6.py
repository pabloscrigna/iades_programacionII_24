"""
pasar un tipo de dato python a string json
"""

import json


foo = False      # true
bar = False     # false

print(f"type foo: {type(foo)}")
print(f"foo: {foo}")

foo_json = json.dumps(foo)

print(f"type foo_json: {type(foo_json)}")
print(f"foo: {foo_json}")


"""
pasar un tipo de dato python a string json
"""

foo_original = json.loads(foo_json)


print(f"type foo original: {type(foo_original)}")
print(f"foo original: {foo_original}")

