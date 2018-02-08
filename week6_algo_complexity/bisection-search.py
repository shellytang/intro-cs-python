# bisection search - implementation 1

# not constant -- we are making a copy of the list in either case and making another copy in the next recursive call
# O(log n) bisection search calls
# O(n) for each bisection search call to copy list
# O(n log n) --> O(n) for a tighter bound

def bisect_search1(L, e):
    if L == []:  # O(1)
        return False
    elif len(L) == 1:  # O(1)
        return L[0] == e
    else: 
        midPoint = len(L)//2
        if L[midPoint] > e:
            return bisect_search1(L[:midPoint], e)  # not constant
        else:
            return bisect_search1(L[midPoint:], e) # not constant

# print(bisect_search1([1, 2, 5, 6, 7], 4))


# implemention 2 -- bisection search with helper
# pass list and indices as parameters
# list never copied, just re-passed
# O(log n)

def bisect_search2(L, e) :

    def bisect_search_helper(L, e, low, high):
        if high == low: # if point is at the same place (only one element), just do the check
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    # base case
    if len(L) == 0:
        return False 
    else: 
        return bisect_search_helper(L, e, 0, len(L) - 1)

print(bisect_search2([1, 2, 4, 5, 6, 7], 4))