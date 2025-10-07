import json
data={
    "userID" :7,
    "id":135,
    "title":"Bond"
}
# f = open("myJsonfile.json","a")
with open("myjsonfile.json","a") as f:
    json.dump(data,f,indent=4) # here indent means space howmany sapce you add
