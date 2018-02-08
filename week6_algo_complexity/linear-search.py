# linear search on sorted list

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:  # sorted
            return False
    return False

# O(n) for the loop and O(1) for the lookup to test if e == L[i]
# overall complexity is O(n) where n is len(L)