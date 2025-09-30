
honest={'VADAPAV':30,'DABELI':40,'BURGAR':70, 'PIZZA':199}
print("\t---MENUE0---")
for k,v in honest.items():
    print(f"\t{k} = {v}")
qty=0
order=input("Enter your order : ").upper()

if order in honest:
    qty=int(input("enter you quantity : "))
    print(honest[order]*qty)
else:
    print("item not found")
        
