import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1] # extract last element of that list
    
    def getLastName(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(month, day, year)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        # returns self current age in days
        return (datetime.date.today() - self.birthday).days
    
    # sort people by last name or first name is same last name
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

p1 = Person('Zoey Cat')
p1.setBirthday(2, 1, 18)
p2 = Person('Eva Cat')
p2.setBirthday(1, 3, 18)
personList = [p1, p2]
personList.sort() # our method as defined in our person class
for e in personList:
    print(e)