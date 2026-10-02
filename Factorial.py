
def Factorial(fn):
    factor=1
    for i in range(1,fn+1):
        factor*=i
    return factor

N=int(input("Enter Number for factorial: "))
res= Factorial(N)
smallestfactor = 0
for i in range(2,N+1):
    if N%i==0:
        smallestfactor=i
        break

primeflag = "Prime" if N==smallestfactor else "none"

print(f"{N}! = {res}")
print(f"smallest factor > 1: {N} ({primeflag})")