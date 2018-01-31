# error if not grade for a student
# OPTION 1: flag error by printing a message

def get_stats(class_list):
    new_stats = []
    for item in class_list:
       new_stats.append([item[0], item[1], avg(item[1])])
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data') # this will print out and it will return none and append to list

# test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], [['bruce', 'wayne'], [10.0, 8.0, 74.0]]]
test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]], [['deadpool'], []]]

print(get_stats(test_grades))
