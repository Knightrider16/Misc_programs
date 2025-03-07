def hanoi(n,initial,temp,final):
    if n==1:
        print(f"Move disk 1 from {initial} to {final}")
        final.append(initial.pop())
        print(f"{initial}\n{final}")
    else:
        hanoi(n-1,initial,final,temp)
        print(f"Move disk {n} from {initial} to {final}")
        final.append(initial.pop())
        print(f"{initial}\n{final}")
        hanoi(n-1,temp,initial,final)

n=int(input("Enter the number of disks: "))
initial=list(range(n,0,-1))
temp=[]
final=[]

print(f"Initial state: {initial}, Temp: {temp}, Final: {final}")
hanoi(n,initial,temp,final)
print(f"Final state: {final}")
