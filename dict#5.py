phonebook={}
n=int(input("Enter total no.of friends:"))
i=1
while(i<=n):
    a=input("Enter Name: ")
    b=int(input("Enter Phone Number: "))
    i = i + 1
phonebook[a]=b
print(" ")

name=input("Enter Name to Search:")
f=0
k=phonebook.keys()
for i in k:
    if(i==name):
        print("Phone number= ",phonebook[i])
    f=1
    if (f==0):
        print("Given name not exist")