#Python Program for Common Divisors of Two Numbers

Num1 = int(input("Enter input number 1: "))
Num2 = int(input("Enter input number 2: "))

for i in range(1, min(Num1, Num2)+1):
    if Num1%i==0 and Num2%i==0:
        print(i)
