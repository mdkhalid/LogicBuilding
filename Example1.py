A=10 
B=3
print(f"Sum={A+B}, Diff={A-B}, Product={A*B}, Quotient={int(A/B)}")

temp=A
A=B
B=temp
print(f"Swap with temp: A={A}, B={B}")

A=10
B=3
A=A+B
B=A-B
A=A-B

print(f"Swap without temp: A={A}, B={B}")
