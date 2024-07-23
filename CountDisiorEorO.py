#Python Program to Check if count of divisors is even or odd using

Num = int(input("Enter input number : "))
Counter = 0

for i in range(1,Num+1):
    if(Num%i==0):
        Counter = Counter + 1

if Counter % 2 == 0:
    print("count of divisors is even")
else:
    print("count of divisors is odd")

