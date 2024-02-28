from random import randint
from time import perf_counter


def find_min(l):
    # find min and max by looping through the whole list and compares the number
    start_time = perf_counter()
    min = l[0]

    for i in l:
        if min > i:
            min = i
    
    final_time = perf_counter() - start_time
    return final_time, min

def find_max(l):
    # find min and max by looping through the whole list and compares the number
    start_time = perf_counter()
    max = l[0]

    for i in l:
        if max < i:
            max = i
    
    final_time = perf_counter() - start_time
    return final_time, max

l = []
for _ in range(0, 2500):
    l.append(randint(1, 3000))

time_taken, min = find_min(l)
print(f"2500 elements:\n\tmin: {min}\n\ttime taken: {time_taken}")

time_taken, max = find_max(l)
print(f"2500 elements:\n\tmax: {max}\n\ttime taken: {time_taken}")

l = []
for _ in range(0, 5000):
    l.append(randint(1, 5500))

time_taken, min = find_min(l)
print(f"5000 elements:\n\tmin: {min}\n\ttime taken: {time_taken}")

time_taken, max = find_max(l)
print(f"5000 elements:\n\tmax: {max}\n\ttime taken: {time_taken}")

# the time complexity of both finding min and max are O(n) because the algorithm works by iterating through the whole list once.
