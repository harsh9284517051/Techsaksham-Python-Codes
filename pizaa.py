s, p, c = input("Size (S/M/L): ").upper(), input("Pepperoni (Y/N): ").upper(), input("Cheese (Y/N): ").upper()
b = {'S': 15, 'M': 20, 'L': 25}[s] + (2 if p == 'Y' and s == 'S' else 3 if p == 'Y' else 0) + (1 if c == 'Y' else 0)
print(f"Total: ${b}")