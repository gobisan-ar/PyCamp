def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)
bar(toast='nah', spam=4, eggs=2)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
