from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3


print("Iterable?[1,2,3]:", isinstance([1, 2, 3], Iterable))
print("Iterable? g():", isinstance(g(), Iterable))

# list iter
print('for x in [1,2,3,4,5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)
