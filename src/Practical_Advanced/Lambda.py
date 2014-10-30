fun=lambda s: s*2
print(fun(8))

fun=lambda s: s**2
print(fun(8))

def myFun(a):
    return lambda s: s**a

fun=myFun(3)
print(fun(8))