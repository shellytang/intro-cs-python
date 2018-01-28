def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

testList = [1, -4, 8, -9]

def getAbs(a):
    return abs(a)

print(applyToEach(testList, getAbs)) # [1,4,8,9]

def square(a):
    return a**2

print(applyToEach(testList, square)) # [1,16,64,81]