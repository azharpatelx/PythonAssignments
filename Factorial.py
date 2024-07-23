#Python Program to find factorial of given number

Num = int(input("Enter input number : "))
Fact = 1

if Num < 0:
    print("Factorial does not exist for negative numbers")
elif Num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, Num + 1):
        Fact = Fact * i
    print("The factorial of",Num,"is",Fact)