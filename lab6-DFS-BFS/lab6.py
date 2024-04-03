graph2 = { "a" : ["d","f"],
"b" : ["c","b"],
"c" : ["b", "c", "d", "e"],
"d" : ["a", "c"],
"e" : ["c"],
"f" : ["a"]
}

def dfs(graph, start):
    visited = []
    unvisited = [start]
    while len(unvisited) > 0:
        i = unvisited.pop()
        if i not in visited:
            visited.append(i)
            unvisited.extend(graph[i])

    return visited

def bfs(graph, start):
    visited = []
    unvisited = [start]
    while len(unvisited) > 0:
        i = unvisited.pop(0)
        if i not in visited:
            visited.append(i)
            unvisited.extend(graph[i])
    
    return visited

print("DFS: ", dfs(graph2, 'a'))
print("BFS: ", bfs(graph2, 'a'))
