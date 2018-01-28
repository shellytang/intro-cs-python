# tuples are an ordered sequence of elements (can be indexed) that can contain 
# mix of element types, are immutable, and represented by parens
def getData(aTuple):
  nums = ()
  words = ()
  for t in aTuple:
    nums = nums + (t[0],) # note the , for single element
    if t[1] not in words:  
      words = words + (t[1],) # concat tuples
  minNum = min(nums)
  maxNum = max(nums)
  uniqueWords = len(words)
  return (minNum, maxNum, uniqueWords)
# binding to return more than one value from a function
(small, large, words) = getData(((1, 'mine'), (3, 'yours'), (5, 'ours'), (7, 'mine')))

