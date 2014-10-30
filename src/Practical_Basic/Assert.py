a=20

try:
    assert a>10
except AssertionError:
    print('a<10')
else:
    print('a>=10')