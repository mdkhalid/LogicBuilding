N=int(input("Enter Number: "))
is_Prime=True

for i in range(2,int(N**0.5)+1):
    if N%i==0:
        is_Prime=False
        break

if is_Prime:
    print("Prime")
else:
    print("Not Prime")

# nothing has been changed