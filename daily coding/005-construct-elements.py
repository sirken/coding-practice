'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

# pair
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def left(x, y):
        return x
    return f(left)

def cdr(f):
    def right(x, y):
        return y
    return f(right)

def car(f):
    return f(lambda x, y: x)

def cdr(f):
    return f(lambda x, y: y)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

###############################

# Trying with a list
def cons(l):
    def lst(f):
        return f(l)
    return lst

def car(f):
    def left(l):
        return l[0]
    return f(left)

def cdr(f):
    def right(l):
        return l[-1]
    return f(right)

def car(f):
    return f(lambda l: l[0])

def cdr(f):
    return f(lambda l: l[-1])


print(car(cons([1, 2, 3, 4])))
print(cdr(cons([1, 2, 3, 4])))
