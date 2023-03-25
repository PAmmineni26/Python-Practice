phonebook={}
n=int(input("Enter Total No.of friends:"))
i=1
while(i<=n):
    a=input("Enter Name: ")
    b=int(input("Enter Phone Number: "))
    i+=1
phonebook[a]=b
print(phonebook)