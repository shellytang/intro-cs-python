import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1] # extract last element of that list
    
    def getLastName(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

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

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign (belongs to the class, not instance)
    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        self.idNum = Student.nextIdNum # student attribute (unique ID)
        Student.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting student uses their ID not name
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.name + " says: " + utterance) 

# Substitution principle
class Student(MITPerson):
    pass # pass is a special keyword, says there is no expression in the body
class UnderGrad(Student):
    def __init__(self, name, classYear):
        Student.__init__(self,name)
        self.year = classYear
    
    def getClass(self):
        return self.year

    def speak(self, utterance):
        return Student.speak(self, " Hiiiii, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

# test for superclass, checks for instances of subclasses
def isStudent(obj):
    # refactored to create a superclass student to prevent from chaining long list
    # return isinstance(obj, UnderGrad) or isinstance(obj, Grad)
    return isinstance(obj, Student)

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self,name)
        self.department = department
    
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic) # note the self


s1 = UnderGrad('Shelly T', 2007)
s2 = UnderGrad('Jessica T', 2007)
s3 = Grad('Carlee M')
print(s1)
print(s1.getClass())
print(s1.speak('wheres the pizza'))
prof1 = Professor('Harry Henderson', 'History')
print(prof1.speak('howdy'))
print(prof1.lecture('hi there'))
# p1 = Person('Zoey Cat')
# p1.setBirthday(2, 1, 18)
# p2 = Person('Eva Cat')
# p2.setBirthday(1, 3, 18)
# personList = [p1, p2]
# personList.sort() # as defined in our person class
# student1 = Student('Imma Student')
# Person.setBirthday(student1, 3, 1, 90)
# student2 = Student('Anna Student')
# Person.setBirthday(student2, 2, 1, 88)
# student3 = Student('Student Three')
# Person.setBirthday(student3, 1, 15, 50)
# studentList = [student1, student2, student3]
# for e in studentList:
#     print(e) 
# studentList.sort() # sort by ID
