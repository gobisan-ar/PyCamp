# **kwargs: Many keyword arguments - optional

def printer(**kwargs):
    print(kwargs)
    print(kwargs["num"])
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key)
        print(value)


printer(num=3, ltr="X")


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)