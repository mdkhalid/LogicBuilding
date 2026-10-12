A, C, D= map(int, input().split())
resons=[]

# print(A, C, D)

if A<18:
    resons.append("Too Young")

if C==0:
    resons.append("Not a Citizen")
if D==1:
    resons.append("Disqualified")

if len(resons)==0:
    print("Eligible")
else:
    print("Not Eligible - "+", ".join(resons))