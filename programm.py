name = input("Enter your name: ")
username=input("Enter your username: ")
number=(input("Enter Number:"))
age=int(input("Enter Age:"))
if name[0]!=" " and name[-1]!=" " and " " in name and "@" in username and "." in username and username[0]!="@" and len(number)==10 and number[0]!="0"and age>=18 and age<=60 and number.isdigit():

 print("User profile is valid")
else:
    print("User profile is invalid")













