#predominantly used functions in prod code:

items=[1,2,3]

def sqr(x):
    return x*x

print map(sqr,items)
print map(lambda x:x*x,items)
print filter(lambda x:x<3,items)
print reduce(lambda x,y:x+y,items)
