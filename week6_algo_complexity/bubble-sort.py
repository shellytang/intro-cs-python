# O(n^2) complexity for nested loops
# inner for loop is doing the comparisons
# outer while loops is for doing multiple passes until no more swaps

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

print(bubble_sort([10,5,6,4]))