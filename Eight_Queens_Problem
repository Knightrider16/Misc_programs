import random

def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col or \
           board[i]-i==col-row or \
           board[i]+i==col+row:
            return False
    return True

def solve_8_queens(n=8):
    def solve(board,row):
        if row==n:
            solutions.append(board[:])
            return
        for i in range(n):
            if is_safe(board,row,i):
                board[row]=i 
                solve(board,row+1)  
                board[row]=-1  

    board=[-1]*n
    solutions=[]
    solve(board,0)
    return solutions

def print_solution(solution):
    n=len(solution)
    for i in range(n):
        board_row=['Q' if col==solution[i] else '.' for col in range(n)]
        print(" ".join(board_row))

solutions=solve_8_queens()
if solutions:
    random_solution=random.choice(solutions)
    print("Solution:")
    print_solution(random_solution)
else:
    print("No solution found.")
