#Check the given number is prime or not

n = int(input("Enter the number : "))
f = 0
if(n == 0) or (n == 1):
    print("Not prime number")
else:
    for i in range(2,n,1):
        if(n % i == 0):
            f = 1
    if(f == 0):
        print("Prime number")
    else:
        print("Not prime number")

