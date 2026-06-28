n = int(input("Enter the first number"))
N = int(input("Enter the second number"))
O = input("Enter operation sign")

if O == "+":
   print(n + N)
elif O == "-":
   print(n - N)
elif O == "*":
   print(n * N)
elif O == "//":
   print(n // N)
elif O == "%":
   print(n % N)      
else:
    print("Coming Soon kid!")   