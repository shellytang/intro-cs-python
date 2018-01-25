# Euclidean algorithm. 
# Suppose that a and b are two positive integers - if b = 0, then answer is a. 
# otherwise, gcd(a,b) is same as gcd(b, a % b)

def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if(b == 0):
        return a
    return gcdRecur(b, a % b)

print(gcdRecur(9,12))


