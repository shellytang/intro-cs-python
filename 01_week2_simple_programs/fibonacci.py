# f(n) = f(n-1) + f(n-2)

def fib(x):
  ''' 
  assumes x an int >= 0
  returns Fibonacci of x
  '''
  # base case
  if x == 0 or x == 1:
    return 1

  else: 
    return fib(x-1) + fib(x-2)