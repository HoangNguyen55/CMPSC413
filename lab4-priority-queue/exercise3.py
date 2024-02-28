class Heap:
    def __init__(self, indexRule) -> None:
        self.heap = []
        # min/max heap can be make depending on the indexRule
        # greater than or less than
        self.op = indexRule

    def __str__(self) -> str:
        return self.heap.__str__()

    def parent(self, i):
        return int((i-1)/2)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def compare_parent(self, i):
        return self.op(self.heap[i][1], self.heap[self.parent(i)][1])

    def compare_priority(self, l, r):
        return self.op(self.heap[l][1], self.heap[r][1])

    def move_up(self, i):
        # compare to parent and move up if it is in violation
        # continues until theres no more violation
        while i > 0 and self.compare_parent(i):
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def move_down(self, i):
        index = i
        while True:
            left = self.left(index)
            right = self.right(index)
            if left < len(self.heap) and self.compare_priority(left, index):
                index = left
            if right < len(self.heap) and self.compare_priority(right, index):
                index = right
            
            if index != i:
                self.swap(i, index)
                i = index
            else:
                break


    # in the worst case, new inserted element have the most priority, the append of new element in python is O(1) so it is unimportant, the function have to move it from the last item of the array to position the root, since this is a tree data structure the element only have to travel half of the array to reach the top, which mean it take O(logn)
    def insert(self, item, priority):
        self.heap.append((item, priority))
        self.move_up(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) == 0:
            return None

        return self.heap[0]

    # in the worst case, the last item that take the root place have to traverse back to the last place, it would still only take O(logn) to traverse to the bottom
    def delete(self):
        if len(self.heap) == 0:
            return None

        val = self.heap[0]
        # swap place to avoid popping 0th position
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.move_down(0)
        return val

    # in the worse case, which is the last element are what needed to be change, the function uses O(n) linear search to find the item we're looking for, then it move the item up or down depending on its new priority which is O(logn) so in total it is O(n + logn), after simplification it is O(n)
    def changePriority(self, item, newPriority):
        index = -1
            
        for i, k in enumerate(self.heap):
            if k[0] == item:
                index = i
                break
        
        # we didn't find the item, terminate early
        if index == -1:
            return
        
        self.heap[index] = (item, newPriority)
        if self.compare_parent(index):
            self.move_up(index)
        else:
            self.move_down(index)

minq = Heap(lambda x, y: x < y)
q = Heap(lambda x, y: x > y)

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
