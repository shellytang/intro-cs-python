# overall complexity of merge sort is O(n log(n)) where n is len(L)

# merge stage is O(n) 
def merge(left, right):
    result = []
    i, j = 0, 0
    # left and right sublists are ordered - move indices for sublists depending on which sublist holds next smallest element
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # when right sublist is empty, copy rest of left sublist
    while i < len(left):
        result.append(left[i])
        i += 1
    # when left sublist is empty, copy rest of right sublist
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    # base case
    if len(L) < 2: # if 1 or less elements, return copy of list
        return L[:]
    else:
        middle = len(L)//2 # dividing list in half is O(log n)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right) # run the merge step

print(merge_sort([8,4,1,6,5,9,2,0]))
