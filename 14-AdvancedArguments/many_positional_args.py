# *args: Many Positional Arguments - optional

def printer(*args):
    print(args)
    print(args[0])
    print(type(args))

    for n in args:
        print(n)


printer(1, 2, 3)


def add(*args):
    tot = 0
    for n in args:
        tot += n
    return tot


add(5, 4, 9)
