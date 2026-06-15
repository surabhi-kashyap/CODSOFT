n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))
op=input("Enter the operator (+,/,*,%) : ")
if op=="+":
    print(n1+n2)
elif op=="/":
    print(n1/n2)
elif op=="*":
    print(n1*n2)
elif op=="%":
    print(n1%n2)
else:
    print("Invalid Operator")
    