# items left of the suffixSt pointer are sorted
# stop when suffixSt is the length of the list, meaning all items are sorted
# O(n^2) -- nested loops where n is len(L)

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

print(selection_sort([5,9,15,1,4]))