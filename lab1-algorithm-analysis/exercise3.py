from random import randint
from time import perf_counter

def find_min(i, j):
    return i if i < j else j

def find_max(i, j):
    return i if i > j else j

def divide_n_conquer(array, start, end, compare):
    if end - start <= 1:
        return array[start]
    else:
        mid = (end + start) // 2
        first = divide_n_conquer(array, mid, end, compare)
        second = divide_n_conquer(array, start, mid, compare)
        return compare(first, second)

l = []
for _ in range(0, 2500):
    l.append(randint(1, 3000))

start_time = perf_counter()
min = divide_n_conquer(l, 0, len(l), find_min)
time_taken = perf_counter() - start_time
print(f"2500 elements:\n\tmin: {min}\n\ttime taken: {time_taken}")

start_time = perf_counter()
max = divide_n_conquer(l, 0, len(l), find_max)
time_taken = perf_counter() - start_time
print(f"2500 elements:\n\tmax: {max}\n\ttime taken: {time_taken}")

l = []
for _ in range(0, 5000):
    l.append(randint(1, 5500))

start_time = perf_counter()
min = divide_n_conquer(l, 0, len(l), find_min)
time_taken = perf_counter() - start_time
print(f"5000 elements:\n\tmin: {min}\n\ttime taken: {time_taken}")

start_time = perf_counter()
max = divide_n_conquer(l, 0, len(l), find_max)
time_taken = perf_counter() - start_time
print(f"5000 elements:\n\tmax: {max}\n\ttime taken: {time_taken}")
