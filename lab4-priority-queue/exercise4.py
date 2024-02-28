class Heap:
    def __init__(self, indexRule, lst=None) -> None:
        # min/max heap can be make depending on the indexRule
        # greater than or less than 
        self.op = indexRule

        if lst == None:
            self.heap = []
        else:
            # in place heapifies
            self.heap = lst
            for i in range(len(lst)//2, -1, -1):
                self.move_down(i)

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
        return self.op(self.heap[i], self.heap[self.parent(i)])

    def compare(self, l, r):
        return self.op(self.heap[l], self.heap[r])

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
            if left < len(self.heap) and self.compare(left, index):
                index = left
            if right < len(self.heap) and self.compare(right, index):
                index = right
            
            if index != i:
                self.swap(i, index)
                i = index
            else:
                break

    def insert(self, item):
        self.heap.append(item)
        self.move_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None

        val = self.heap[0]
        # swap place to avoid popping 0th position
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.move_down(0)
        return val

# There are two part of this, first part is building the heap which is done in-place, it work by traversing the half array, which would take O(n/2) time, and moving down each element which would take O(logn) time, in total it take O(n/2 * logn), so in total it is O(nlogn) time after simplification
# the second part is getting the min/max value by delete(), which take O(logn) time, in total it take O(nlogn + logn), or O(nlogn) after simplification
# the function uses the same step for both min and max (ascending/decending) sort, so they both took the same time
def heap_sort(heap):
    i = heap.delete()
    sorted = []
    while i != None:
        sorted.append(i)
        i = heap.delete()
    return sorted

from random import randint

lst = []
for _ in range(10):
    lst.append(randint(0, 100))

print("List: ", lst)

minheap = Heap(lambda x, y: x < y, lst.copy())
maxheap = Heap(lambda x, y: x > y, lst.copy())
print("Heapifing...")
print("Min heap: ", minheap)
print("Max heap: ", maxheap)
print("Sorting...")
print("Ascending:", heap_sort(minheap))
print("Descending:", heap_sort(maxheap))

