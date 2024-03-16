""" Fibonacci numbers module
        (c)2024  Henrique Moreira
"""

# pylint: disable=missing-function-docstring,invalid-name

# In mathematics, the Fibonacci numbers form a sequence such that:
#	a) each number is the sum of the two preceding numbers,
#	   starting from 0 and 1.
# That is Fn = Fn-1 + Fn-2, where F0 = 0, F1 = 1, and n >= 2.
# The sequence formed by Fibonacci numbers is called the Fibonacci sequence.

def fibonacci(n):
    """ return Fibonacci series up to n """
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result

def fib2(n):
    """ Alternative Fibonacci series up to n """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def fib_non_zero(seq_nr=10):
    """ Fibonacci sequence up to 'seq_nr' """
    if seq_nr <= 0:
        return []
    result = [1]
    a, b = 0, 1
    while len(result) < seq_nr:
        if a > 1:
            result.append(a)
        a, b = b, a + b
    return result

# Print Fibonacci sequence up to 55:
#	print([(idx, num) for idx, num in enumerate(fibonacci(55))])
#
# First 10 numbers in the Fibonacci sequence:
#	print([(idx, num) for idx, num in enumerate(fib_non_zero(10), 1)])
