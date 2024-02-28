from random import randint

def linear_search(item, l):
    for i, val in enumerate(l):
        if item == val:
            return i
    return -1

# Linear search search through the whole list once so its time worst complexity is O(n), It's best time complexity is when the first element it look through is what it want, so O(1)

def binary_search(item, l):
    max = len(l)
    min = 0
    # get middle
    index = max//2
    while True:
        if(max - min <= 1):
             # didn't find anything return -1
             return -1
        if(l[index] == item):
            # find it, return position
            return index
        elif(l[index] > item):
            # current element is bigger than what we need
            # so ignore everything to the right
            max = index
        else:
            # current element is smaller than what we need
            # so ignore everything to the left
            min = index

        # get middle
        index = (min + max)//2

# Binary search, search through the list cutting it in half each iteration so it's worst time complexity is O(logn), best case is the first item it look at being the item it want so O(1)

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            temp = l[j]
            l[j] = l[j-1]
            l[j-1] = temp
            j=j-1
    
    return l

# insertion employs two loops going from start til the end so its O(n) * O(n) which result in O(n^2), but with it's best care where the list is already sorted it only need to go through the list once, so O(n)

def selection_sort(l):
    # loop through the whole thing
    for i in range(0, len(l)):
        min = i
        # find minimum
        for j in range(i, len(l)):
            if l[min] > l[j]:
                min = j

        # swap place with minimum
        if min != i:
            temp = l[i]
            l[i] = l[min]
            l[min] = temp

    return l

# selection also uses two loops going from start til end so its O(n^2), in the best case where the list is already sorted this function still need to perform all of the same procedure, so it is still O(n^2)

def bubble_sort(l):
    sort = False
    while not sort:
        sort = True
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                sort = False
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp

    return l

# Bubble sort also uses two loops, with the inner loop going from start til end, the outer loop won't terminate until the whole list have been sorted, in the worst case where theres only one pair that are sorted per iteration an additional O(n) are needed, so O(n) * O(n) = O(n^2), in the best care where the list is already sorted it only need to go through the list once, so O(n)

l = []
for _ in range(20):
    l.append(randint(0, 20))

print("Linear: 6")
print(l)
print("index:", linear_search(6, l))
print("Binary (sorted): 6")
l.sort()
print(l)
print("index:", binary_search(6, l))

l = []
for _ in range(20):
    l.append(randint(0, 20))
print("Insertion")
print(l)
print(insertion_sort(l))
l = []
for _ in range(20):
    l.append(randint(0, 20))
print("Selection")
print(l)
print(selection_sort(l))
l = []
for _ in range(20):
    l.append(randint(0, 20))
print("Bubble")
print(l)
print(bubble_sort(l))
