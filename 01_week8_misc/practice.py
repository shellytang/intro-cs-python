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


# Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). This function returns the length of the longest run of monotonically increasing numbers occurring in L. A run of monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.
# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].

def longestRun(L):
  if len(L) == 0:
    return 0
    
  maxLen = 1
  currentLen = 1
  
  for i in range(len(L)-1):
    if L[i] <= L[i+1]:
        currentLen += 1
    else:
        currentLen = 1
    if currentLen >= maxLen:
        maxLen = currentLen
  return maxLen

# L = []
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print(longestRun(L))

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    
    key_code = {}
    for i in range(len(map_from)):
      key_code[map_from[i]] = map_to[i]
    
    result = ''
    for letter in code: 
      result += key_code[letter]
    
    return (key_code, result)
  
print(cipher("abcd", "dcba", "dab")) 
# ({'a': 'd', 'b': 'c', 'c': 'b', 'd': 'a'}, 'adc')