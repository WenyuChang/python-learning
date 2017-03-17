__author__ = 'wenychan'

"""
Apply function to every item of iterable and return a list of the results.

If additional iterable arguments are passed, function must take that many arguments
and is applied to the items from all iterables in parallel.

If one iterable is shorter than another it is assumed to be extended with None items.

If function is None, the identity function is assumed;

if there are multiple arguments, map() returns a list consisting of tuples containing the
corresponding items from all iterables (a kind of transpose operation). The iterable arguments
may be a sequence or any iterable object; the result is always a list.

map(f, sequence) is directly equivalent to: [f(x) for x in sequence]
map(f, sequence1, sequence2) is equivalent to: [f(x1, x2) for x1, x2 in zip(sequence1, sequence2)]
"""


def func(x1, x2):
    return '%s : %s' % (x1, x2)
print map(func, [1,3,5,7,9], [2,4,6,8,10])