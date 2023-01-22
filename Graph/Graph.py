class Graph:
    def __init__(self,edges,n):

        self.adjList = [[] for _ in range(n)]

        for (src,dst) in edges:
            self.adjList[src].append(dst)

def printGraph(graph):

    for src in range(len(graph.adjList)):
        for dst in graph.adjList[src]:
            print(f'{src}->{dst}',end=" ")

        print()

edges = [(0,1),(1,2),(2,3),(3,0),(0,2),(0,3),(1,0),(2,0),(3,0),(2,1),(3,2)]
n=4
grap = Graph(edges,n)
printGraph(grap)