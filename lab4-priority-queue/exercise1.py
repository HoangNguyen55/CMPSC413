class PriorityQueue():
    def __init__(self):
        self.queue = []

    def __str__(self) -> str:
        return self.queue.__str__()
    def __getitem__(self, idx):
        i =  len(self.queue) - idx - 1
        if i < 0:
            raise IndexError
        return self.queue[i]
    # Binary Search
    def _search(self, search_item):
        max = len(self.queue)
        min = 0
        index = max//2
        while True:
            if(max - min <= 1):
                # return the closest index when looking for priority
                return index
            if(self.queue[index][1] == search_item):
                return index
            elif(self.queue[index][1] > search_item):
                max = index
            else:
                min = index

            index = (min + max)//2

    def _search_item(self, item):
        for i, k in enumerate(self.queue):
            if k[0] == item:
                return i

        return -1

    # In the worse case, which is inserting at the front everytime.
    # The function uses binary search to find the appropriate location, which take O(logn) of time, then it insert the element, which is O(n) in python, in total the function takes O(logn + n) time, which is O(n) after simplification.
    def insert(self, item, priority):
        if len(self.queue) == 0:
            self.queue.append((item, priority))
        else:
            i = self._search(priority)
            if(priority > self.queue[i][1]):
                self.queue.insert(i+1, (item, priority))
            else:
                self.queue.insert(i, (item, priority))

    def peek(self):
        return self.queue[-1]

    # In the worst case, and the only case, because the function are already sorted, the delete function return the last item in the array, since the delete function uses python pop() function which have an O(1) time, the function have O(1) time also.
    def delete(self):
        return self.queue.pop()

    # In the worse case, the item we need to change for are the last.
    # This function uses linear search to look for the item which have O(n), then it remove that element, which is also O(n), and insert it again with the new priority, which is O(n), so in total this function take O(n + n + n), which is O(3n), after simplification it is O(n)
    def changePriority(self, item, priority):
        # search for location
        i = self._search_item(item)
        if(i != -1):
            self.queue.pop(i)
            self.insert(item, priority)


class MinPriorityQueue(PriorityQueue):
    def _search(self, search_item):
        max = len(self.queue)
        min = 0
        index = max//2
        while True:
            if(max - min <= 1):
                return index
            if(self.queue[index][1] == search_item):
                return index
            elif(self.queue[index][1] < search_item):
                max = index
            else:
                min = index

            index = (min + max)//2

    def insert(self, item, priority):
        if len(self.queue) == 0:
            self.queue.append((item, priority))
        else:
            i = self._search(priority)
            if(priority < self.queue[i][1]):
                self.queue.insert(i+1, (item, priority))
            else:
                self.queue.insert(i, (item, priority))

minq = MinPriorityQueue()
q = PriorityQueue()

for i in range(5):
    minq.insert(i, i*10)
    q.insert(i, i*10)

print("="*10)
print("Max queue before: ")
print(q)
print("Insert item: '5' with priority of '10'")
q.insert(5, 10)
print("Max queue after: ")
print(q)

print("="*10)
print("Max queue before: ")
print(q)
print("Remove element with highest priority")
print("Get:", q.delete())
print("Max queue after: ")
print(q)

print("="*10)
print("Max queue before: ")
print(q)
print("Change priority of '5' to 500")
q.changePriority(5, 500)
print("Max queue after: ")
print(q)

print("="*10)
print("="*10)
print("Min queue before: ")
print(minq)
print("Insert item: '5' with priority of '10'")
minq.insert(5, 10)
print("Min queue after: ")
print(minq)

print("="*10)
print("Min queue before: ")
print(minq)
print("Remove element with lowest priority")
print("Get:", minq.delete())
print("Min queue after: ")
print(minq)

print("="*10)
print("Min queue before: ")
print(minq)
print("Change priority of '5' to 500")
minq.changePriority(5, 500)
print("Min queue after: ")
print(minq)
