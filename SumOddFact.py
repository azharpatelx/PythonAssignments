#Python Program to find sum of odd factors of given number

Num = int(input("Enter input number : "))

def Sum_Odd_Fact(Num):
    Sum = 0
    for i in range(1, Num+1):
        if Num % i == 0 and i % 2 != 0:
            Sum = Sum + i
    print("Sum of odd factors of",Num,"are:",Sum)
     
Sum_Odd_Fact(Num)

