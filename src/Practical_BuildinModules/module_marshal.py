__author__ = 'wenychan'

import marshal
# cannot handle class instances, shared element and recursive data structures
# use pickle to handle above things.

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
)

data = marshal.dumps(value)
# intermediate format
print type(data), len(data)
print repr(data)

print "#"*50
print marshal.loads(data)

print '#'*100