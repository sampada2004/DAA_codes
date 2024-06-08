def bfs(src, adj):
    n = len(adj)
    visited = [0] * n 
    queue = [src]  
    visited[src] = 1  

    while queue:
        curr = queue.pop(0) 
        print(curr) 
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                queue.append(neighbor)  
                visited[neighbor] = 1  
adjacency_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

source_vertex = 0
bfs(source_vertex, adjacency_list)

            