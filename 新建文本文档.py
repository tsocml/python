import time
def performance(f):
    def fn(*args, **kwargs):
        t1 = time.time()
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return f(*args,**kwargs)
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))