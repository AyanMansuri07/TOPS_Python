gmail=input("enter gmail : ")
if gmail.islower():
    if gmail.endswith("@gmail.com"):
        print("Valid Gmail address")
    else:
        print("Invalid Gmail address")
else:
    print("Invalid Gmail address")


