# take tampurature value value  0 and 100 water , more than 100  air, bilove 0 cold

tempure = int(input("Enter the tempurature : "))

if tempure >=0 and tempure <= 100:
    print("water ")
elif tempure >100:
    print("air")
else:
    print("cold")