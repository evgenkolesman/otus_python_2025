import math
import np


def share_bread(N, K):
    # your code here
    x = K // N
    y = K - x * N
    return x, y


# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
assert share_bread(N=3, K=14) == (4, 2)


def leap_year(year_to_check):
    if year_to_check % 4 == 0 and (year_to_check % 100 != 0 or year_to_check % 400 == 0):
        return 'YOU SHALL PASS'
    else:
        return 'YOU SHALL NOT PASS'


assert leap_year(5) == 'YOU SHALL NOT PASS'


def amulet_area(a, b, c):
    # your code here
    p = (a + b + c) / 2

    return math.sqrt(p * (p - a) * (p - b) * (p - c))


assert amulet_area(3, 4, 5) == 6


def cal_euclidean(a, b):
    ## Your code here
    return np.linalg.norm(a - b)

def cal_manhattan(a, b):
    ## Your code here
    distance = 0
    for p_i,q_i in zip(a,b):
        distance += abs(p_i - q_i)

    return distance

def cal_cosine(a, b):
    ## Your code here
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

a = np.random.randint(-10, 10)
b = np.random.randint(-10, 10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))