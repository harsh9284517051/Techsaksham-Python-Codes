def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Divison by zero wrong :"
    return a/b

def calculator():
    print("choose:")
    print("1:addition")
    print("1:subtraction")
    print("1:multiplication")
    print("1:divison")
    
ch=input("Enter A choice : from (1,2,3,4,)")
if ch in ('1','2','3','4'):
    num1=float(input("Enter First Number"))
    num2=float(input("Enter Second Number "))
    
    if ch=='1':
        print("Result :",add(num1,num2))
    elif ch=='2':
        print("Result :",subtract(num1,num2))
    elif ch=='1':
        print("Result :",multiply(num1,num2))
        
    elif ch=='3':
        print("Result :",divide(num1,num2))
        
else:
    print("inavlid Choice")
    
calculator()
        