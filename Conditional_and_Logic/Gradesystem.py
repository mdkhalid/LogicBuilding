S=int(input("Enter number: "))

if S<=100 and S>=90:
    print("A")
elif S<=89 and S>=75:
    print("B")
elif S<=74 and S>=60:
    print("C")
elif S<=59 and S>=50:
    print("D")
elif S<50:
    print("Fail")
else:
    print("Provide correct number")
