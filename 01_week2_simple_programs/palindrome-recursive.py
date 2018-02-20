def isPalindrome(s):
  # clean up chars to lowercase and remove spaces
  def cleanUpChars(s):
    s = s.lower()
    ans = ''
    for char in s:
      if char in 'abcdefghijklmnopqrstuvwxyz':
        ans += char
    return ans
  
  def checkPal(s):
    # base case
    if len(s) <= 1:
      return True
    else:
      # check first and last and check by slicing out everything but first and last and checking if true
      return s[0] == s[-1] and checkPal(s[1:-1])
  
  return checkPal(cleanUpChars(s))

print(isPalindrome('Able was I, ere I saw Elba'))