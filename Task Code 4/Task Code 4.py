# 1 Second Largest Element
def second_largest(arr):
    unq = []

    for i in arr:
        if i not in unq:
            unq.append(i)

    if len(unq) < 2:
        return None

    largest = max(arr)
    arr.remove(largest)
    return max(arr)

arr = [5, 4, 54, 2, 76]
print(second_largest(arr))
from email.utils import encode_rfc2231
from operator import truediv


#2 Depth Limited Search (DLS)
def dls_recursion(graph, node, goal, lim):
        if lim < 0:
            return False
        if node == goal:
            return True
        for i in graph.get(node, []):
            if dls_recursion(graph, i, goal, lim - 1):
                return True
        return False

def dls(graph, start, goal, lim):
    return dls_recursion(graph, start, goal, lim)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C', 'P'],
    'P': ['G'],
    'H': ['D']
}

start = 'A'
goal = 'P'
depth_limit1 = 2
depth_limit2 = 3

if dls(graph, start, goal, depth_limit1):
    print("Goal node is reached with depth limit " + str(depth_limit1))
else:
    print("Goal node cannot be reached with depth limit " + str(depth_limit1))

if dls(graph, start, goal, depth_limit2):
    print("Goal node is reached with depth limit " + str(depth_limit2))
else:
    print("Goal node cannot be reached with depth limit " + str(depth_limit2))