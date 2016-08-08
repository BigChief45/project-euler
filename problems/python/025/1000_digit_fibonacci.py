### Jaime Alvarez - March 2016

"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    
    a = 1
    b = 1
    c = 0
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        
    return c

if __name__ == '__main__':
    digits = 0
    index = 1

    while True:
        fib = fibonacci(index)
        
        # Check digits
        digits = len(str(fib))
        if digits == 1000:
            print "Index of first Fibonacci term to contain 1000 digits: ", index
            break
        
        index += 1

