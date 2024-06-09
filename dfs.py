graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = set() 
def dfs(visited, graph, node):   
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Enter the starting node for Depth-First Search:")
start_node = input().strip()
print("Following is the Depth-First Search:")
dfs(visited, graph, start_node)

            