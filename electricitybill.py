def calcultebill(units):
    if units<=200:
        bill=0
    elif units <= 500:
        bill=(units-200)*8
    elif units<=1000:
        bill=(300*8)+(units-500)*11
    else:
        bill=(300*8)+(500*11)+(units-1000)*14
    return bill
while True:
    units = int(input("Enter the number of units consumed (Enter -1 to exit): "))
    if units == -1:
        break  # Exit the loop when -1 is entered
    bill_amount = calcultebill(units)
    print(f"Total electricity bill for {units} units: Rs. {bill_amount}")
