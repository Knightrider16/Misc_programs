from collections import deque

def bfs(graph,start,end):
    visited={start}
    queue=deque([(start,[start])])    
    while queue:
        node,path=queue.popleft()       
        if node==end:
            return path
        
        for neighbor in range(len(graph)):
            if graph[node][neighbor]!=0 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,path+[neighbor]))   
    return None  

def find_eulerian_circuit(graph,start):
    stack=[start]
    circuit=[]
    while stack:
        current=stack[-1]
        for neighbor in range(len(graph)):
            if graph[current][neighbor]>0:
                stack.append(neighbor)
                graph[current][neighbor]-=1
                graph[neighbor][current]-=1
                break
        else:
            circuit.append(stack.pop())
    return circuit

def chinese_postman_problem(graph):
    odd_degree_nodes=[i for i,row in enumerate(graph) if sum(row)%2!=0]
    if len(odd_degree_nodes)==0:
        print("Graph has an Eulerian circuit. No extra edges needed.")
        start=0  
        circuit=find_eulerian_circuit(graph,start)
        return circuit

    odd_pairs=[]
    min_added_length=float('inf')
    for i in range(len(odd_degree_nodes)):
        for j in range(i+1,len(odd_degree_nodes)):
            u=odd_degree_nodes[i]
            v=odd_degree_nodes[j]
            path=bfs(graph,u,v)
            if path:
                path_length=len(path)-1  
                odd_pairs.append((u,v,path,path_length))

    added_edges=[]
    total_added_length=0
    while odd_pairs:
        u,v,path,path_length=min(odd_pairs,key=lambda x:x[3])
        added_edges.append((path,path_length))
        total_added_length+=path_length
        odd_pairs=[p for p in odd_pairs if p!=(u,v,path,path_length)]

    for path, _ in added_edges:
        for i in range(len(path)-1):
            u=path[i]
            v=path[i+1]
            graph[u][v]+=1
            graph[v][u]+=1
    start=0  
    circuit=find_eulerian_circuit(graph,start)
    return circuit

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

circuit=chinese_postman_problem(graph)
print("Eulerian Circuit:",circuit)
