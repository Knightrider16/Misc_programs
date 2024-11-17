from itertools import permutations

def tsp(distances,city_names=None):
    n=len(distances)
    cities=list(range(n))
    shortest_path=None
    min_cost=float('inf')

    for i in permutations(cities[1:]): 
        current_path=[0]+list(i)+[0] 
        cost=sum(distances[current_path[i]][current_path[i+1]] for i in range(n))
        
        if cost<min_cost:
            min_cost=cost
            shortest_path=current_path

    if city_names:
        path_description="->".join(city_names[city] for city in shortest_path)
        detailed_steps=[
            f"{city_names[shortest_path[i]]} to {city_names[shortest_path[i+1]]}:{distances[shortest_path[i]][shortest_path[i+1]]} units"
            for i in range(len(shortest_path)-1)
        ]
    else:
        path_description="->".join(str(city) for city in shortest_path)
        detailed_steps=[
            f"{shortest_path[i]} to {shortest_path[i+1]}:{distances[shortest_path[i]][shortest_path[i+1]]} units"
            for i in range(len(shortest_path)-1)
        ]

    return path_description,min_cost,detailed_steps

distances = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]
city_names=["A","B","C","D"]  
path,cost,steps=tsp(distances,city_names)
print(f"Path:{path}")
print(f"Total Cost:{cost} units")
for step in steps:
    print(step)
