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

# implementation of a flexible greedy
#keyFunction defines an ordering of the elements of items and uses this
# ordering to decide what we mean by "best" (best to worst with reverse = True)
def greedy(items, maxCost, keyFunction):
    '''Assumes items is a list, maxCost >= 0, keyFunction maps elements of items to numbers'''
    # sorted is a function that returns a list
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print('    ', item)

# using greedy
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUse greedy by cost to allocate ', maxUnits, ' calories')
    # sort from least expensive to most expensive (get inverse of getCost)
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x)) 

    print('\nUse greedy by density to allcoate ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apples', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
