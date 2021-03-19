print("Enter name: ")
name = input()

if len(name)<3:
     print("name is not 3 characters")
elif len(name)>50:
    print("name is more than 50 characters")
else:
    print("name looks good")
