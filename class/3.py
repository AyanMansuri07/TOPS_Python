class student:
    def inputdata(self,subject,score):
        self.subject = subject
        self.score = score
    def displaydata(self):
        print(f"subject : {self.subject} \n score : {self.score}")

obj  = student()
sub = input("enter the subject : ")
score = int(input("enter the score : "))

obj.inputdata(sub,score)
obj.displaydata()