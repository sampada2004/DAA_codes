answer=[]
def tsp(graph,v,curr_pos,n,count,cost):
    if(count==n and graph[curr_pos][0]):
        answer.append(cost+graph[curr_pos][0])
        return
    for i in range(n):
        if(v[i]==False and graph[curr_pos][i]):
            v[i]=True
            tsp(graph,v,i,n,count+1,cost+graph[curr_pos][i])
            v[i]=False
print("Enter the number of vertices:")
n=int(input())
graph=[]
for i in range(n):
    row=list(map(int,input().strip().split()))
    graph.append(row)
v=[False for i in range(n)]
v[0]=True
tsp(graph,v,0,n,1,0)
print(min(answer))   
