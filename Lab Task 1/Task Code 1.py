def ucs (graph, start, goal):
    frontier = [(0, start, [start])]
    visited = []

    while frontier:
        frontier.sort()
        cost, node, path = frontier.pop(0)

        if node == goal:
            return cost, path
        if node not in visited:
            visited.append(node)

            for neighbour, neighbour_cost in graph.get(node, []):
                if neighbour not in visited:
                    frontier.append((cost + neighbour_cost, neighbour, path + [neighbour]))
    return None, None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start = 'A'
goal = 'D'
cost, path = ucs (graph, start, goal)

if path:
    print(f"The path using UCS becomes : {path} \nAnd cost becomes : {cost}")
else:
    print("No path found")