def count_odd_degrees(graph):
    odd_count=0
    for node in graph:
        if len(graph[node])%2!=0:
            odd_count+=1
    return odd_count

def eulerian_path(graph):
    start_node=None
    for node in graph:
        if len(graph[node])%2!=0:
            start_node=node
            break

    if start_node is None:
        start_node=list(graph.keys())[0]

    path=[]
    stack=[start_node]
    
    while stack:
        current_node=stack[-1]
        if graph[current_node]:
            next_node=graph[current_node].pop()
            stack.append(next_node)
            graph[next_node].remove(current_node)
        else:
            path.append(stack.pop())
    
    return path[::-1] 

konigsberg_graph = {
    'A':['B','C'],  
    'B':['A','C','D'], 
    'C':['A','B','D'], 
    'D':['B','C'] 
}

def eulerian_check(graph):
    odd_degree_count=count_odd_degrees(graph)   
    if odd_degree_count==0:
        return "Eulerian Circuit exists.",eulerian_path(graph)
    elif odd_degree_count==2:
        return "Eulerian Path exists.",eulerian_path(graph)
    else:
        return "No Eulerian Path or Circuit exists.",[]

result,path=eulerian_check(konigsberg_graph)
print(result)
if path:
    print("Eulerian Path/Circuit:","->".join(path))
