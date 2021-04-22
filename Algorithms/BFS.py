from queue import Queue
max = 100
# V = Vertices
# E = Edges
V = None
E = None
visited = [False for i in range(max)]
path = [0 for i in range(max)]
graph = [[] for i in range(max)]

def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    
    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u

# s: starting point
# f: finishing point
def printPath(s, f):
    # no recursion
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print('No Path')
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break

    for i in range(len(b)-1, -1, -1):
        print(b[i], end=' ')

if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0
    f = 4
    BFS(s)
    printPath(s, f)