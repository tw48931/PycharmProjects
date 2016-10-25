import itertools

r = itertools.ifilter(lambda x: x%2==0, itertools.count(1))
for x in itertools.takewhile(lambda x: x<100, r):
    print x