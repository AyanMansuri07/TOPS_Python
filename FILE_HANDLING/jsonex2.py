import json
users = []

for i in range(3):
    obj ={}
    name = input("Enter the name  : ")
    subject = input("Enter the subject : ")
    score=int(input("Enter the score : "))
    
    obj["name"]=name
    obj["subject"]=subject
    obj["score"]=score
    
    users.append(obj)
    
with open("myjson2.json","a") as f:
    json.dump(users,f,indent=4)
    
print("CREATED !!!!!!!!!!!!!!")