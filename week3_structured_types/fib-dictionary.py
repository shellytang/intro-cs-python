# this keeps track of already calculated values instead of recal same values many times

def fib_efficient(n, d):
    # if in is already in dictionary, just lookup and return
    if n in d:  
        return d[n ]
    else:
        # otherwise, do recursive call, store the value and return
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2} # base case
print(fib_efficient(30, d)) # 1346269
