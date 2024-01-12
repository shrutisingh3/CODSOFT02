def add(P,Q):
    return P+Q
def sub(P,Q):
    return P-Q
def mul(P,Q):
    return P*Q
def div(P,Q):
    return P/Q
def mod(P,Q):
    return P%Q
print("!! This is the Basic Calculator !!")
print("Choose operations:  ")
print(" 1.addition\n 2.subtract\n 3.multiply\n 4.divide\n 5.module")
choice=input("Enter your choice(1/2/3/4/5):  ")
if choice > '5':
    print("Invalid Input Please choose another number!! ")
else:
    n1=int(input("enter the first number: "))
    n2=int(input("enter the second number: "))
    if choice=='1':
        print(n1,"+",n2,"=",add(n1,n2))
    elif choice=='2':
        print(n1,"-",n2,"=",sub(n1,n2))
    elif choice=='3':
        print(n1,"*",n2,"=",mul(n1,n2))
    elif choice=='4':
        print(n1,"/",n2,"=",div(n1,n2))
    elif choice=='5':
        print(n1,"%",n2,"=",mod(n1,n2))
