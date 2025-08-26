status = True
while status:
    name = input("Eneter your name : ")
    choice=input("Do you whant to add more name ? press 'y' for add and 'n' no ")
    if choice == 'y' or choice == 'yes':
        status = True
    else:
        status=False
