x = int(input("Enter Your Number: "))
i = 0
while x>=1:
    i += 1
    if i % 2 == 0 and x > i:
        print(i)