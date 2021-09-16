# reduce() = apply a function to an iterable and reduce it to a single comulative value.
#            performs function on first 2 elements and repeats until only 1 element remains
# reduce(function, iterable)

import functools

letters = ("H", "E", "L", "L", "O")

word = functools.reduce(lambda x, y: x+y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]

result = functools.reduce(lambda x, y: x*y, factorial)
print(result)
