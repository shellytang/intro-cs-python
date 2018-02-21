# decision tree implementation
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items,
    avail a weight
    Returns a tuple of the total value of a solution to
    0/1 knapsack problem and the items of that soultion"""

    if toConsider == [] or avail == 0:
        result = (0, ()) # return no value and items if list is empty
    elif toConsider[0].getCost() > avail:
        # if item to consider is too heavy/big, then we will slice it out and call maxVal
        result = maxVal(toConsider[1:], avail)
    else: # otherwise, we can take it - so we'll look at left and right branch
        nextItem = toConsider[0]
        # left branch - take it - we remove/slice it from toConsider and update the available weight
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue() # increase withVal with value of that item
        # right branch - if we don't take the item - don't update avail
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
    # test left branch and right branch 
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate ', maxUnits, ' calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken = ', val)
    if printItems:
        for item in taken:
            print('    ', item)


class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
    
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ': < ' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    '''names, values, calories lists of same length. 
    name is a list of strings
    values and calories are lists of numbers
    returns list of Foods'''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apples', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testMaxVal(foods, 750)