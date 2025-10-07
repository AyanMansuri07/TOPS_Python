l1 = ["python","java","android","php"]
try:
    index = int(input("enter the index : "))
    print(l1[index])
except IndexError:
    print("indxe not found")
except ValueError:
    print("Invalid input")
