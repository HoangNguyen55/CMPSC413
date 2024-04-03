from typing import Any


dense_graph = {
    'A': [('B', 2), ('C', 1), ('D', 3)],
    'B': [('A', 2), ('C', 4), ('D', 2)],
    'C': [('A', 1), ('B', 4), ('D', 5)],
    'D': [('A', 3), ('B', 2), ('C', 5)]
}
dense_graph2 = {
    'A': [('B', 2), ('C', 1), ('D', 3), ('E', 4)],
    'B': [('A', 2), ('C', 4), ('D', 2), ('E', 3)],
    'C': [('A', 1), ('B', 4), ('D', 5), ('E', 2)],
    'D': [('A', 3), ('B', 2), ('C', 5), ('E', 1)],
    'E': [('A', 4), ('B', 3), ('C', 2), ('D', 1)]
}
sparse_graph = {
    'A': [('B', 2), ('F', 3), ('E', 1)],
    'B': [('A', 2), ('C', 4)],
    'C': [('B', 4), ('D', 2)],
    'D': [('C', 2)],
    'E': [('A', 1)],
    'F': [('A', 3)]
}


# O(n)
def sort_all_edges(graph):
    edges = []
    # O(n) or O(n^2) for dense undirected graph
    for key in graph.keys():
        for dest, cost in graph[key]:
            edges.append((key, dest, cost))
    # O(nlogn)
    edges.sort(key=lambda x: x[2])
    return edges

# O(e + v)
def dfs_is_cycle(mst, edge):
    visited = []
    unvisited = [edge[1]]
    while unvisited:
        path = unvisited.pop()
        if path not in visited:
            visited.append(path)
            unvisited.extend(p for p in mst.get(path, []))
        if edge[0] in visited:
            return True
    return False

def kruskal(graph: dict):
    mst = {}
    sorted_edges = sort_all_edges(graph) 
    for i in sorted_edges:
        if not dfs_is_cycle(mst, i):
            val = mst.get(i[0], None)
            if val == None:
                mst[i[0]] = (i[1], i[2])
            elif val[1] > i[2]:
                mst[i[0]] = (i[1], i[2])
    return mst

class Heap:
    def __init__(self, indexRule) -> None:
        self.heap = []
        self.op = indexRule

    def __str__(self) -> str:
        return self.heap.__str__()

    def __len__(self):
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


    def insert(self, item, priority):
        self.heap.append((item, priority))
        self.move_up(len(self.heap) - 1)

    def delete(self):
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.move_down(0)
        return val

def prims(graph, start: str):
    mst: dict = {}
    visited = set()
    heap = Heap(lambda x, y: x < y)
    for i in graph[start]:
        heap.insert((start, i[0]), i[1])

    while len(heap) > 0:
        edge, cost = heap.delete()
        if edge[1] not in visited:
            visited.add(edge[1])
            mst[edge[0]] = (edge[1], cost)
            for i in graph[edge[1]]:
                if i[0] not in visited:
                    heap.insert((edge[1], i[0]), i[1])
    
    return mst
#
# print(kruskal(dense_graph))
# print(kruskal(dense_graph2))
# print(kruskal(sparse_graph))
print(prims(dense_graph, 'A'))
print(prims(dense_graph2, 'A'))
print(prims(sparse_graph, 'A'))
