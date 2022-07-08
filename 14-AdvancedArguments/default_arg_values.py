# Default values for arguments

def foo(a, b=4, c=6):
    print(a, b, c)


foo(1)
foo(4, 9)
foo(1, 7, 9)
foo(20, c=6)
