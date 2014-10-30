__author__ = 'wenychan'

# Changes in Python 3.0
#
# The way import operations in packages work has changed slightly in Python 3.0. This change applies only to
# imports within files located in the package directories we’ve been studying in this chapter; imports in other
# files work as before. For imports in packages, though, Python 3.0 introduces two changes:
#
# 1. It modifies the module import search path semantics to skip the package’s own directory by default.
#    Imports check only other components of the search path. These are known as “absolute” imports.
#
# 2. It extends the syntax of from statements to allow them to explicitly request that imports search the
#    package’s directory only. This is known as “relative” import syntax.