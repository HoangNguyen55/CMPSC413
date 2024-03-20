class Heap:
    def __init__(self, indexRule) -> None:
        self.heap = []
        self.op = indexRule

    def __str__(self) -> str:
        return self.heap.__str__()

    def length(self):
        return len(self.heap)

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


    #O(logn)
    def insert(self, item, priority):
        self.heap.append((item, priority))
        self.move_up(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) == 0:
            return None

        return self.heap[0]

    #O(logn)
    def delete(self):
        if len(self.heap) == 0:
            return (None, 0)

        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.move_down(0)
        return val

    #O(n)
    def changePriority(self, item, newPriority):
        index = -1
            
        for i, k in enumerate(self.heap):
            if k[0] == item:
                index = i
                break
        
        if index == -1:
            return
        
        self.heap[index] = (item, newPriority)
        if self.compare_parent(index):
            self.move_up(index)
        else:
            self.move_down(index)

class Node():
    def __init__(self, val, right= None, left= None) -> None:
        self.val = val
        self.right = right 
        self.left = left

# O(n)
def calculate_freq(string):
    freq = {}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    return freq

def sort_by_freq(freq):
    minq = Heap(lambda x, y: x < y)
    for i in freq:
        minq.insert(Node(i), freq[i])
    return minq

def build_huffman_tree(minq: Heap):
    while minq.length() > 1:
        l = minq.delete()
        r = minq.delete()
        prio = l[1] + r[1]
        root = Node(None, l[0], r[0])
        minq.insert(root, prio)

    val = minq.delete()[0]
    if val:
        return val
    raise Exception("")

def build_code_tree(node: Node, _code = ""):
    tree_map = {}
    if node.val:
        return {node.val: _code}

    if node.left and node.right:
        tree_map.update(build_code_tree(node.left, _code + "0"))
        tree_map.update(build_code_tree(node.right, _code + "1"))

    return tree_map

def encode_file(file):
    encoded_text = ""
    encoded_tree = None
    with open(file) as f:
        text = f.readline().rstrip()
        encoded_tree = build_huffman_tree(sort_by_freq(calculate_freq(text)))
        encode_table = build_code_tree(encoded_tree)
        for i in text:
            encoded_text +=  encode_table[i]
    return encoded_text, encoded_tree

def decode_text(text, root_node: Node):
    final_text = ""
    val: Node | None = root_node
    for i in text:
        if i == "0":
            val = val.left # type: ignore
        elif i =="1":
            val = val.right # type: ignore
        if val.val != None: # type: ignore
            final_text += val.val # type: ignore
            val = root_node
    return final_text


freq = calculate_freq("ABAAABCBCCCDEFFFEE")
minq = sort_by_freq(freq)
node = build_huffman_tree(minq)
codes = build_code_tree(node)

encoded_text, encoded_table = encode_file("test.txt")
print(decode_text(encoded_text, encoded_table))
