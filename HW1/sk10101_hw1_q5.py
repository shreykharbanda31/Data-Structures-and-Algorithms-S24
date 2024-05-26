def fibs(n):
    x=0
    y=1
    yield x+y
    for i in range(1,n):
        a=x+y
        yield a
        x=y
        y=a


