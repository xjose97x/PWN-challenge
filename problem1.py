from time import sleep, time
from math import trunc

"""
Returns a humanized string from seconds
"""
def humanize_seconds(seconds):
    seconds = round(seconds, 4)
    milliseconds = str(seconds).split('.')[1] if isinstance(seconds, float) else 0
    seconds = trunc(seconds)

    minutes = seconds // 60
    seconds -= minutes * 60

    hours = minutes // 60
    minutes -= hours * 60

    result = ''
    if hours:
        unit = 'hour' if hours == 1 else 'hours'
        result += f'{hours} {unit} '
    if minutes:
        unit = 'minute' if minutes == 1 else 'minutes'
        result += f'{minutes} {unit} '
    if seconds:
        unit = 'second' if seconds == 1 else 'seconds'
        result += f'{seconds} {unit} '
    if milliseconds:
        unit = 'millisecond' if milliseconds == 1 else 'milliseconds'
        result += f'{milliseconds} {unit}'
    return result 


"""
Decorator that times a function execution and prints it in a humanized way
"""
def timer(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print('Time elapsed: ' + humanize_seconds(end - start))
        return result
    return wrapper


@timer
def test_function(delay):
    sleep(delay)


"""
The solution provided is a decorator.
The benefit of this solution is that it can be used to any existing function in any codebase
and it will just work :)

Example usage:
> test_function(1)
Time elapsed: 1 second 0001 milliseconds
"""
