age=int(input("How old are you?"))
if age<13:
    print("You are a preteen")
elif age>=13 and age<=19:
    print("You are a teenager")
elif age>=20 and age<=120:
    print("You are an adult")
else:
    print("This is not a valid age")
