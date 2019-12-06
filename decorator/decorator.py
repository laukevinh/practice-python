"""Examples of using decorators. See more details at 
https://realpython.com/primer-on-python-decorators
"""

#Decorators
def do_twice(func):
    def wrapper():
        a = func()
        b = func()
        return a, b
    return wrapper

def do_twice_with_args(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        b = func(*args, **kwargs)
        return a, b
    return wrapper

def header(text):
    def custom_greeting(func):
        def wrapper(*args, **kwargs):
            return text, func(*args, **kwargs)
        return wrapper
    return custom_greeting

#Functions
def generic_greeting():
    return "Hello world!"

def personal_greeting(name):
    return "Hello {}!".format(name)

#Functions with decorators
@do_twice
def greet_twice():
    return "This uses the `do_twice` decorator."

@do_twice_with_args
def greet_twice_by_name(name):
    return ("{}, this uses the `do_twice_with_args` decorator".format(name))

@header("This is a header")
def greet_by_name_with_header(name):
    return ("{}, this uses the `header` decorator".format(name))
