import math
import numpy

# Ex 1

def share_bread(N, K):
    # your code here
    x = K // N
    y = K - x * N
    return x, y

assert share_bread(N=3, K=14) == (4, 2)

# Ex 2


def leap_year(year_to_check):
    if year_to_check % 4 == 0 and (year_to_check % 100 != 0 or year_to_check % 400 == 0):
        return 'YOU SHALL PASS'
    else:
        return 'YOU SHALL NOT PASS'


assert leap_year(5) == 'YOU SHALL NOT PASS'

# Ex 3


def amulet_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


assert amulet_area(3, 4, 5) == 6

# Ex 4

def cal_euclidean(a, b):
    return numpy.linalg.norm(a - b)

def cal_manhattan(a, b):
    return abs(a - b)


def cal_cosine(a, b):
    return numpy.dot(a, b) / (numpy.linalg.norm(a) * numpy.linalg.norm(b))

a = numpy.random.randint(-10, 10)
b = numpy.random.randint(-10, 10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))

# Ex 5

my_array = numpy.random.rand(100)
print(numpy.max(my_array), numpy.min(my_array))
print(my_array)

my_array = numpy.random.randint(low=0, high=51, size=(5, 6))
selected_column = my_array.argmax(axis=1)
print('Shape: ',my_array.shape)
print('Array')
print(my_array)
print(selected_column)

def unique_rows(X):
    rows_tuples = [tuple(row) for row in X]
    unique_tuples = list(set(rows_tuples))
    unique_matrix = numpy.array(unique_tuples)
    return unique_matrix


X = numpy.random.randint(4, 6, size=(10,3))
print(X)
print(unique_rows(X))