#Program to find the factroial provided by user
n=int(input("Enter Your Number: "))
factorial = 1
if n < 0:
    print("Factorial For -ve numbers doesn't Exist")
elif n==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial = factorial * i
    print("The Factorial of", n, "is" ,factorial)
