from functools import  wraps

def decorator(func):
    def inner(*args, **kwargs):
        print(f'start decorator')
        func(*args, **kwargs)
        print('finish decorator')
    return inner

def say(name):
    print(f'hello {name}')

say = decorator(say)
say('adsf')


def header(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print(f'<h1>')
        func(*args, **kwargs)
        print('<h2>')
    return inner


def table(func):
    def inner(*args, **kwargs):
        print(f'<table>')
        func(*args, **kwargs)
        print('</table>')
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@table
# @header
def say(name, surname, age):
    '''
    print name surname and age
    :param name:
    :param surname:
    :param age:
    :return:
    '''
    print(f'hello {name} {surname} {age}')

say('nax', 'asdf', 98)
help(say)
print(say.__name__, say.__doc__)