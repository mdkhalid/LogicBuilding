N=int(input("Enter Natural Number: "))
Sum=0
for i in range(1,N+1):
    Sum+=i

print(f"For loop: {Sum}")

Sum=0
i=1
while(i<=N):
    Sum+=i
    i+=1

print(f"While loop: {Sum}")

Sum=int(N*(N+1)/2)

print(f"Formula: {Sum}")
