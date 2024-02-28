from random import randint

def find_first_nonrepeat(l):
    # find the first element by iterating through the whole list and compare one element with the rest of the element
    for i, n in enumerate(l):
        not_repeat = True 
        for j, k in enumerate(l):
            # compare one element with the rest
            # if there is repeats we don't need to continue, so set a flag and break out of the loop
            if n == k and i != j:
                not_repeat = False
                break 

        # if found a number not repeating then return its position
        if not_repeat:
            return i

    return -1

# create a randomize list
l = []
for _ in range(1, 15):
    l.append(randint(0, 9))
i = find_first_nonrepeat(l)
print(l)
print(f"first non repeat number position: {i}\nfirst non repeat number value: {l[i]}")

# the time complexity of this algorithm are O(n^2), because this method employ two loops which in the worse case scenerio it will have to check each element with all the other element for all element.
