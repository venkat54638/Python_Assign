# Easy function
# first function
def filter_even_numbers(num):
    result = []
    for i in num:
        if i % 2 == 0:
            result.append(i)
    return result
#Test cases
print(filter_even_numbers([1,2,3,4,5,6]))
print(filter_even_numbers([1,3,5,]))

# second function
def merge_sorted_lists(list1,list2):
    list1.extend(list2)  
    return sorted(list1)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))

# Medium function
# First function
def generate_martix(m,n):
    result = []
    for i in range(m):
        rows = []
        for j in range(n):
            rows.append((i*j))
        result.append(rows)
    return result

#Test cases
martix = generate_martix(3, 3)
for row in martix:
    print(row)
# second function

def transpose_matrix(matrix):
    transpose =[]
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose

#test cases
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
x = transpose_matrix(matrix)
for row in x:
    print(row)

#Hard function
# first function
def find_peaks(num):
    peaks = []
    for i in range(1, len(num) - 1):
        if num[i] > num[i - 1] and num[i] > num[i + 1]:
            peaks.append(i)
    return peaks
#Test cases
print(find_peaks([1, 3, 2, 3, 5, 4, 3, 2, 3, 1]))
#second function
def rotate_list(lst, k):
    n = len(lst)
    if k > n:
        return lst[::-1]
    if k ==0:
        return lst
    k = k % n
    rotate = []
    for i in range(n-k,n):
        rotate.append(lst[i])
    for i in range(n-k):
        rotate.append(lst[i])
    return rotate
#Test cases
print(rotate_list([1, 2, 3, 4, 5], 2)) 
print(rotate_list([1, 2, 3], 4)) 





