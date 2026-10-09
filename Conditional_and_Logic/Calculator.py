
isContinue=True

while(True):
    N1=int(input("Enter Number 1: "))
    N2=int(input("Enter Number 2: "))
    Operation=input("Enter Operations +-/*%: ")

    if Operation not in ["+", "-", "/", "*", "%"]:
        print("Invalid operator. Try again.")
        continue
    if Operation=="+":
        print(f"Add: {N1+N2}")
    if Operation=="-":
        print(f"Substract: {N1-N2}")
    if Operation=="*":
        print(f"Multiplication: {N1*N2}")
    if Operation=="/":
        if N2==0:
            print("Divide by Zero Exception")
        else:
            print(f"Division: {N1/N2}")
    if Operation=="%":
        print(f"Remainder: {N1%N2}")

    Que = input("Do you want to continue operation: Y/N ").lower()

    if Que!="y":
        isContinue=False
     

