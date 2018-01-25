def gcdIter(a, b):
    '''
    a, b: positive integers 
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # test with the smaller value
    testValue = min(a,b)
    
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    
    return testValue

print(gcdIter(9,12))