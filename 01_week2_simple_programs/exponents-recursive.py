# recursive solution for returning exponential base

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Base case
    if exp <= 0:
        return 1

    return base * recurPower(base, exp - 1)

print(recurPower(2,4))