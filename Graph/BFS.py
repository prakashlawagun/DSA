#Breadth First Search

from   collections import deque

def bfs(graph,root):
    visted,queue = set(),deque([root])
    visted.add(root)

    while queue:
        vertex = queue.popleft()

        print(str(vertex)+" ",end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in  visted:
                visted.add(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS Traversal",end="\n")
    bfs(graph,'A')
