# Easy function
#first question
def swap_pairs(num):
    num = list(num)
    for i in range(0, len(num)-1, 2):
        num[i], num[i+1] = num[i+1], num[i]
    return tuple(num)
#test cases
print(swap_pairs((1, 2, 3, 4)))  
print(swap_pairs((1, 2, 3)))  
#second question
def get_stats(num):
    result = []
    a = min(num)
    result.append(a)

    b = max(num)
    result.append(b)

    c = sum(num)
    result.append(c)

    d = sum(num) / len(num)
    result.append(d)

    return tuple(result)

# Test case
print(get_stats([1, 2, 3, 4, 5]))

#Medium function
#first question
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade'])

def top_student(student):
    def average(grades):
        return sum(grades) / len(grades)
    return max(student, key=lambda s: average(s.grade))
alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))

#second functions
def count_coordinate_occurrences(coordinates):
    count = {}
    for coord in coordinates:
        if coord in count:
            count[coord] += 1
        else:
            count[coord] = 1
    return count
# Test case
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))

#hard function
#first question
def group_by_department(employee):
    department_dict = {}

    for name, department, salary in employee:
        if department not in department_dict:
            department_dict[department] =  {
                'total_salary': 0,
                'count': 0,
                'names': []
            }
        department_dict[department]['total_salary'] += salary
        department_dict[department]['count'] += 1
        department_dict[department]['names'].append(name)
    result = []
    for department, data in department_dict.items():
        average_salary = data['total_salary'] / data['count']
        result.append((department, average_salary, data['names']))
    return result
# Test case
employees = [
    ("Alice", "Engineering", 80000),
    ("Bob", "Marketing", 70000),
    ("Charlie", "Engineering", 90000),
    ("Diana", "HR", 65000),
    ("Eve", "Marketing", 75000)
]

result = group_by_department(employees)
print(result)

    
