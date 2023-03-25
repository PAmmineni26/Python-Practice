#Write a python program to accept and surname of a student,Save it as student name
#(A)Display the first 4 chars of the student name
#(B)Display the lenght of the name and surname
#(C)Display the name in reverse order
#(D)Every 4th letter of the name
#(E)Every 2nd letter in reverse order

x=input("Enter Your Name: ")
y=input("Enter Your Surnmae: ")
z=x + y
print("Student Name: " , z)
print("First 4 letter of the Student Name: ",z[0:4])
print("Lenght of the Name: ",len(x))
print("Lenght of the Surname: ",len(y))
print("Reverse order of the name: ",z[-1:-len(z):-1])
print("4th letter of String:",z[0:len(z)+1:4])
print("2nd letter in Reverse order: ",z[-1:-len(z):-2])