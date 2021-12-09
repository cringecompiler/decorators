import sys
from time import gmtime, strftime


def my_write(string_text):
    if string_text == '\n':
        pass
    else:
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        original_write('[' + now + ']' + ': ' + string_text + '\n')


def timed_output(function):
    def wrapper(name):
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        sys.stdout.write('[' + now + ']' + ': ')
        function(name)
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


def redirect_output(filepath):
    def decorator(function):
        def wrapper():
            stdout = sys.stdout
            try:
                sys.stdout = open(filepath, 'w')
                function()
            finally:
                sys.stdout.close()
                sys.stdout = stdout
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    original_write = sys.stdout.write
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write

    print_greeting('Nikita')

    calculate()
