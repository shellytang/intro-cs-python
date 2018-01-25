# count the number of time 'bob' appears in a string
s = 'bobabcbobbob'
count = 0
for index in range(len(s)):
  if s[index:index+3] == 'bob':
    count += 1 
print('Number of times bob occurs is: ' + str(count))


