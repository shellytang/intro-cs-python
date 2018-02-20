# error if not grade for a student
# OPTION 2: change the policy

def get_stats(class_list):
    new_stats = []
    for item in class_list:
       new_stats.append([item[0], item[1], avg(item[1])])
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0 # decided that students w/o grades get a 0

# test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], [['bruce', 'wayne'], [10.0, 8.0, 74.0]]]
test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]], [['deadpool'], []]]

print(get_stats(test_grades))
