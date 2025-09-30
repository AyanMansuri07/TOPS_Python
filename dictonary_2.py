student={'name' : 'Ayan Mansuri','subject' : 'python', 'score' : 98}

for k,v in student.items():
    print(f"{k} = {v}")
    
print("--------------------------------------------------")
for k in student.keys():
    print(k)
print("--------------------------------------------------")
for v in student.values():
    print(v)