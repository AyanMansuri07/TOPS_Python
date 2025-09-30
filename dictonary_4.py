quiz = {
    1 : {
        "que" : "which language is most popular ?",
        "ans" : "Python"
        } ,
    2 : { 
        "que" : "who is the prime minister of india ?",
        "ans" : "Narendra Modi"
    } 
}
# print(quize[1]["que"])
for i in range(1,len(quiz)+1):
    print(f"Que.({i}) {quiz[i]["que"]} ")
    ans = input("enter you answer : ").capitalize()
    
    if ans == quiz[i]["ans"]:
        print("right answer ")
    else:
        print("Wrong answer !")