N=int(input("Enter Digits: "))

count=0
total=0

while N>0:
    digit=N%10
    total = total+digit
    count = count+1

    N=N//10


print(N)
print(count)
print(total)

