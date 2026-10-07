N=int(input("Enter Natural Number: "))

reverse=0

while N>0:
    digit=N%10

    reverse = reverse*10+digit

    N= N//10


print(reverse)