def genOneMillion():
    maxNum = 1000000
    current = -1
    while current < maxNum:
        current += 1
        yield current
# range essentially
test = genOneMillion()
print(test.__next__())
print(test.__next__())
print(test.__next__())
