# Python Program to check if binary representation of a number is palindrome or not 

Num = int(input("Enter input number : "))

def Checkbinpalindrome(num): 
    binary = bin(num)
    binary = binary[2:] 
    print("Binary of:", num, "is", binary)
    if binary == binary[-1::-1]:
        print("Binary of:", num, "is palindrome")
    else:
        print("Binary of:", num, "is not palindrome")

Checkbinpalindrome(Num)