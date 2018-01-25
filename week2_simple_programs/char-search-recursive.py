# check if a letter is in an alpha sorted string using bisection search

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # base case: if string is empty, we did not find match 
    if aStr == '':
        return False

    middleIndex = len(aStr)//2
    middleChar = aStr[middleIndex]

    # base case: if middle character is the match
    if char == middleChar:
        return True

    elif char > middleChar:
        aStr = aStr[(middleIndex+1):]
        return isIn(char, aStr)

    else:
        aStr = aStr[:middleIndex]
        return isIn(char, aStr)

    return isIn(char, aStr)

print(isIn('b', 'aabdejlmruuvv'))