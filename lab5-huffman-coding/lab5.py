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

    #O(logn)
    def delete(self):
        if len(self.heap) == 0:
            return (None, 0)

        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.move_down(0)
        return val

class Node():
    def __init__(self, val, right= None, left= None) -> None:
        self.val = val
        self.right = right 
        self.left = left

# This agorithm loop through the string one by one which make its time complexity is O(n)
def calculate_freq(string):
    freq = {}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    return freq

# This sorting algorithm is done by looping through all of the frequency list, which is an O(n) operation, inserting in a priority queue built with a min heap, the insertion operation is O(logn) in a min heap, over all it is a O(n*logn) operation
def sort_by_freq(freq):
    minq = Heap(lambda x, y: x < y)
    for i in freq:
        minq.insert(Node(i), freq[i])
    return minq

# The huffman tree building agorithm works by repeatedly removing two element, which take O(logn) time, and combining them into a node with left and right side, and add that back in, so in every iteration one element is remove and it is repeat until theres only one element left, which is the huffman tree we want, the time complexity of this would be O(logn*n) which is O(nlogn)
def build_huffman_tree(text):
    minq = sort_by_freq(calculate_freq(text))

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

# building the tree map required for encoding process is done by traversing the huffman tree using DFS algorithm, which is O(v + e) where v is vertecies and e is edges
def build_tree_map(node: Node, _code = ""):
    tree_map = {}
    if node.val:
        return {node.val: _code}

    if node.left and node.right:
        tree_map.update(build_tree_map(node.left, _code + "0"))
        tree_map.update(build_tree_map(node.right, _code + "1"))

    return tree_map

###
# however to to build a huffman tree useable by the encoding and decoding process, the text need to be process by calucating the frequnecy and sorting it, so overall the time complexity would be O(n + nlogn + nlogn), which is O(nlogn) after simplication
# the tree map need to be build for the encoding process, which is requires building the huffman tree, so it take O(nlogn + v + e) time, which is O(nlogn) after simplification
###

# the text can be encode by looping through whole input which is O(n) operation, so time complexity of encoding the text is O(n)
def encode_text(text, tree_map):
    encoded_text = ""
    for i in text:
        encoded_text +=  tree_map[i]
    return encoded_text

# decode the text only requires looping through the input text while following the huffman tree provided, so its time complexity is O(n)
def decode_text(text, huffman_tree: Node):
    final_text = ""
    val: Node | None = huffman_tree
    for i in text:
        if i == "0":
            val = val.left # type: ignore
        elif i =="1":
            val = val.right # type: ignore
        if val.val != None: # type: ignore
            final_text += val.val # type: ignore
            val = huffman_tree
    return final_text

print("-"*50)
print("Task 1:")
input = "ABAAABCBCCCDEFFFEE"
huffman_tree = build_huffman_tree(input)
print(f"Input: {input}")
print("Huffman tree map: ", build_tree_map(huffman_tree))
print("-"*50)
print("Task 2:")
print("Encoding text file: 'test.txt'")
with open('test.txt') as f:
    input = f.readline().rstrip()
    print("input:", input)
    huffman_tree = build_huffman_tree(input)
    encoded_text = encode_text(input, build_tree_map(huffman_tree))
    print("Encoded text: ", encoded_text)
    print("Decoded text: ", decode_text(encoded_text, huffman_tree))
