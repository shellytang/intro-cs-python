# Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.
def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    def reverseStr(aStr):
      if len(aStr) <= 1:
        return aStr
      return reverseStr(aStr[1:]) + aStr[0]
    
    return reverseStr(aString) == aString
    
# print(isPalindrome(''))
# print(isPalindrome('racecar'))
# print(isPalindrome('racetrack'))

