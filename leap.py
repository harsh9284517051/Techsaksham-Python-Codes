year = int(input("Enter A Year : "))
print(f"{year} Is a Leap Year " if (year%4==0 and year % 100 !=0) or (year%400==0) else f"{year} is Not  Leap Year")