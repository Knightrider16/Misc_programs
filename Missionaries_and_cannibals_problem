from collections import deque

def missionaries_and_cannibals():
    start=(3,3,0)  
    final=(0,0,1)   
    queue=deque([(start,[start])])
    visited=set()  
    
    while queue:
        current_state,path=queue.popleft()
        if current_state==final:
            return path
        
        visited.add(current_state)       
        m,c,b=current_state
        moves=[(1,0),(0,1),(1,1),(2,0),(0,2)] 
        
        for move_m,move_c in moves:
            if b==0: 
                new_state=(m-move_m,c-move_c,1)
            else:  
                new_state=(m+move_m,c+move_c,0)
            
            if 0<=new_state[0]<=3 and 0<=new_state[1]<=3:  
                if (new_state[0]==0 or new_state[0]>=new_state[1]):  
                    if (3-new_state[0]==0 or (3-new_state[0]>=3-new_state[1])): 
                        if new_state not in visited:  
                            queue.append((new_state,path+[new_state]))
    
    return None  

def describe_solution(solution):
    steps=[]
    for i in range(len(solution)-1):
        current=solution[i]
        next_state=solution[i+1]
        m_diff=abs(current[0]-next_state[0])
        c_diff=abs(current[1]-next_state[1])
        direction="to the other side" if current[2]==0 else "back to the starting side"
        steps.append(f"Move {m_diff} missionary(ies) and {c_diff} cannibal(s) {direction}.")
    
    return steps

solution=missionaries_and_cannibals()
if solution:
    print("Solution found!")
    steps=describe_solution(solution)
    for i,step in enumerate(steps,1):
        print(f"Step {i}: {step}")
    print("Final state:",solution[-1])
else:
    print("No solution exists.")
