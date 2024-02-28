from time import perf_counter

def linear_search(key, val, l):
    for i, item in enumerate(l):
        if val == item[key]:
            return i
    return -1

def binary_search(key, val, l):
    max = len(l)
    min = 0
    index = max//2
    while True:
        if(max - min <= 1):
             return -1
        if(l[index][key] == val):
            return index
        elif(l[index][key] > val):
            max = index
        else:
            min = index
        index = (min + max)//2

def insertion_sort(key, l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j - 1][key] > l[j][key]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp
            j=j-1
    return l

def selection_sort(key, l):
    
    for i in range(0, len(l)):
        min = i
        for j in range(i, len(l)):
            if l[min][key] > l[j][key]:
                min = j
        if min != i:
            temp = l[i]
            l[i] = l[min]
            l[min] = temp
    return l

def bubble_sort(key, l):
    sort = False
    while not sort:
        sort = True
        for i in range(len(l) - 1):
            if l[i][key] > l[i+1][key]:
                sort = False
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l

def merge_sort(key, l):
    # base case
    if(len(l) <= 1):
        return l
    
    mid = len(l)//2
    left = merge_sort(key, l[:mid])
    right = merge_sort(key, l[mid:])

    temp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    temp.extend(left[i:])
    temp.extend(right[j:])

    return temp 

def parse_text(location):
    database = []
    with open(location, "r") as f:
        lines = f.readlines()
        for line in lines:
            items = line.rstrip().split(',')
            data = {"Student ID": items[0],
                    "first name": items[1],
                    "last name": items[2],
                    "email id": items[3], 
                    "Major": items[4]}
            database.append(data)
    return database

def sort_n_display(key, database, sort_algo):
    print(f"Sorting with '{key}' using:", sort_algo.__name__)
    start = perf_counter()
    db = sort_algo(key, database)
    final = perf_counter() - start
    print(f"Sorting take: {final} ms")
    for i in db:
        print(i)


print("Unsort DB")
db = parse_text("data.txt")
print("Linear search for 'Student ID' of '007': ")
start = perf_counter()
i = linear_search("Student ID", '007', db)
final = perf_counter() - start
print(f"Linear_search take: {final} ms")
print("Found 'Student ID' of '007' at: index", i)
print("Full record is: ", db[i])
print("")
sort_n_display("Student ID", db, selection_sort)
print("")
sort_n_display("Student ID", db, insertion_sort)
print("")
sort_n_display("Student ID", db, bubble_sort)
print("")
sort_n_display("Student ID", db, merge_sort)

print("")
print("Sorting Sorted db")
print("")
db = merge_sort("Student ID", db)
sort_n_display("Student ID", db, selection_sort)
print("")
sort_n_display("Student ID", db, insertion_sort)
print("")
sort_n_display("Student ID", db, bubble_sort)
print("")
sort_n_display("Student ID", db, merge_sort)
print("")

print("Sorting using data with all the same element")
db_same = parse_text("data_same.txt")
sort_n_display("Student ID", db_same, selection_sort)
print("")
sort_n_display("Student ID", db_same, insertion_sort)
print("")
sort_n_display("Student ID", db_same, bubble_sort)
print("")
sort_n_display("Student ID", db_same, merge_sort)
