l1=[1,2,3,4,'abhi']
print(l1)
x=input("Enter your Element Datatype(Str,Int,flt): ")
if x=="Str":
    ele1=input("Enter Your Str value: ")
    if ele1 in l1:
          print("Yes Element is Present in List")
    else:
          print("Your Elemnt is not Present in the List")
elif x=='Int':
    ele2=int(input("Enter Your Int Value: "))
    if ele2 in l1:
          print("Yes Element is Present in List")
    else:
          print("Your Elemnt is not Present in the List")
elif x=="Flt":
    ele3= float(input("Enter Your Float Element: "))
    if ele3 in l1:
        print("Yes Element is Present in List")
    else:
        print("Your Element is not Present in the List")
else:
    print("Invalid Input. Please Give a valid Input")