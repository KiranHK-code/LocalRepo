# display wheather a person is senior citigen or not
name=(input("Enter your name: "))
year=int(input("Enter your birth year: "))
age=int(2024-year)
if age>60:
    print("your a senior citigen",name)
else:
    print("your not a senior citigen",name)