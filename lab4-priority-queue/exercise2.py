class Node():
    def __init__(self, val, next) -> None:
        self.val = val
        self.next: Node = next

    def __str__(self) -> str:
        return f"Node({self.val})"

    def __getitem__(self, idx):
        return self.val[idx]

class LinkedList():
    def __init__(self) -> None:
        self.root = None
        self.max = 0

    def __str__(self) -> str:
        string = "["
        for i in self:
            string += f"{i}, "
        string = string[:-2]
        string += "]"
        return string
        
    def __len__(self):
        return self.max

    def __setitem__(self, pos, val):
        if pos < 0 or pos > self.max:
            raise IndexError(f"Out of bound access, index: {pos}")

        current = self.root
        for _ in range(pos):
            # let LSP ignore none checking because it'll never be None
            current = current.next # type: ignore
   
        current.val = val # type: ignore

    def pop(self, pos = -1):
        if pos >= 0:
            location = pos
        else:
            location = self.max + pos

        if self.root == None:
            return None

        # special edge case for when we want to remove the 1st element
        if pos == 0:
            val = self.root.val
            self.root = self.root.next
            self.max -= 1
            return val

        current = self.root
        index = 0
        while current.next != None and index < location - 1:
            index += 1
            if current.next.next != None:
                current = current.next
            else:
                break

        val = current.next
        current.next = current.next.next
        self.max -= 1
        return val 
        

    def insert(self, val, pos = None):
        if pos == None:
            pos = self.max
        elif pos < 0 or pos > self.max:
            raise IndexError(f"Out of bound access, index: {pos}")

        current = self.root
        previous = None
        index = 0
        if current != None:
            # go through the index
            while index < pos:
                index += 1
                previous = current
                current = current.next # type: ignore

        if previous != None:
            # push the current up by one and replace it's spot
            new_node = Node(val, current)
            previous.next = new_node
        else:
            # push at the begining of the list
            new_node = Node(val, current)
            self.root = new_node

        self.max += 1

    def __getitem__(self, idx):
        if self.root == None:
            return self

        current = self.root
        for _ in range(idx):
            current = current.next
            
        if current == None:
            raise IndexError

        return current

class PriorityQueue():
    def __init__(self):
        self.queue = LinkedList()

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
                return index
            if(self.queue[index][1] == search_item):
                return index
            elif(self.queue[index][1] > search_item):
                max = index
            else:
                min = index

            index = (min + max)//2

    def _search_item(self, item):
        for i, k in enumerate(iter(self.queue)):
            if k[0] == item:
                return i

        return -1

    # In the worse case, which is inserting at the front everytime.
    # The function uses binary search to find the appropriate location, which take O(logn) of time, then it insert the element, which is O(n) in my linked list implementation, in total the function takes O(logn + n) time, which is O(n) after simplification.
    def insert(self, item, priority):
        if len(self.queue) == 0:
            self.queue.insert((item, priority))
        else:
            i = self._search(priority)
            if(priority > self.queue[i][1]):
                self.queue.insert((item, priority), i+1)
            else:
                self.queue.insert((item, priority), i)

    def peek(self):
        return self.queue[-1]

    # In the worst case, and the only case, because the function are already sorted, the delete function return the last item in the array, in my implementation of linked list, in order to make changes to the last element, you first have to traverse the length of the entire list, which make this function O(n)
    def delete(self):
        return self.queue.pop()

    # In the worse case, the item we need to change for are the last.
    # This function uses linear search to look for the item which have O(n), then it remove that element, which is also O(n), and insert it again with the new priority, which is O(n), so in total this function take O(n + n + n), which is O(3n), after simplification it is O(n)
    def changePriority(self, item, priority):
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
                if 1 == 0:
                    return -1 
                else:
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
            self.queue.insert((item, priority))
        else:
            i = self._search(priority)
            if(priority < self.queue[i][1]):
                self.queue.insert((item, priority), i+1)
            else:
                self.queue.insert((item, priority), i)

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
