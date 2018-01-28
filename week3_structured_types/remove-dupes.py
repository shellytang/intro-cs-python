# avoid mutating a list as you are iterating over it. python uses an internal counter to keep
# track of index in the loop, and mutating changes the list length but python doesn't update counter
def removeDupesNew(L1, L2):
    L1_copy = L1[:]  # clone the list first
    for e in L1_copy:
        if e in L2:
          L1.remove(e)
    return L1
  
print(removeDupesNew([1, 2, 3, 4], [1, 2, 5, 6]))