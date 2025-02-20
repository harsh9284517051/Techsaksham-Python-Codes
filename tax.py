def calculatetax(salary,savings):
    decsave=min(savings,200000)
    taxsal=salary-decsave
    
    if taxsal<=1000000:
        return taxsal*0.10
    elif taxsal <=2200000:
        return 100000+(taxsal-1000000)*0.20
    else:
        return 340000+(taxsal-2200000)*0.30
    
while True:
    salary=int(input("Enter Salary Amount (Enter -1 To exit) :"))
    if salary ==-1:
        break
    savings=int(input("Enter Your Saving Amount :"))
    
    tax=calculatetax(salary,savings)
    print(f"For Dalari :{salary},saving :{savings} ->Tax to be Paid :{tax4}")
    