score =0
def increment():
    global score
    score+=10
    print(score)
def decrement():
    global score 
    score -= 10
    
increment()
increment()
decrement()
