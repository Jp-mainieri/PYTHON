def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')

def print_twice(value):
    print(value)
    print(value)

do_twice(print_twice, 'spam')

print('')

def do_four(f, value):
    f(value)
    f(value)

do_four(print_twice, 'spam')