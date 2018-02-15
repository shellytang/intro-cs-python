# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. 
def findLongestSubstr(s):
  longestLen = 0
  longestSubstr = ''
  currentLen = 1
  start = 0
  for i in range(1,len(s)):
    currentLen = i - start
    if(currentLen > longestLen):
        longestLen = currentLen
        longestSubstr = s[start:i]
    if s[i] < s[i-1]:
      start = i
      currentLen = 1
    if s[i] > s[i-1]:
      currentLen += 1
    if s[i] > s[i-1] and i == len(s)-1:
      if(currentLen > longestLen):
        longestLen = currentLen
        longestSubstr = s[start:i+1]
  # return longestSubstr
  print('Longest substring in alphabetical order is: ' + longestSubstr)

# s = 'azcbobobegghakl' # beggh
# s = 'esunlxhtujzjruomfcapp' # esu
# s = 'abcdefghijklmnopqrstuvwxyz'
# s = 'yzvinzrfgtxhpsohvjz' # fgtx
s = 'pdwicgelsoytckghhmk' # ghhm
print(findLongestSubstr(s))

