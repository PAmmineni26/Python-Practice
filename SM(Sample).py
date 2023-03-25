x= input("Enter Your Value: ")
num = len(x)
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print(x[j], end=" ")
    print()
