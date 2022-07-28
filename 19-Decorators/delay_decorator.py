import time

# Simple python decorator functions


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function


# With the @ syntactic sugar

@delay_decorator
def say_hello():
    print('Hello')


say_hello()


@delay_decorator
def say_bye():
    print('Bye')


say_bye()


# Without the @ syntactic sugar

def say_greeting():
    print("How are you ?")


decorated_function = delay_decorator(say_greeting)
decorated_function()