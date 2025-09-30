# KKR = kolkata knight riders
# PBKS = Punjab Knights
# SRH = Sunrisers Hyderabad
# LSG = Lucknow super Gaints
import random
print("\n\t\t-------------------------------------------IPL__2025-------------------------------------------\n")

# ------------------------------------------------------TEAM SELECTION PHASE 1---------------------------------------------------------------

team_list=["CSK","DC","KKR","MI","PBKS","RCB","SRH","LSG"]  # --------------------main all teams list 
print("TEAMS :-- CSK , DC , KKR , MI , PBKS , RCB , SRH , LSG")

user_team = input("Please select your team  :: ").upper() # ---------------------------user select its team
Toss = False

if user_team=="CSK" or user_team=="DC" or user_team == "KKR" or user_team == "MI" or user_team == "PBKS" or user_team == "RCB" or user_team == "SRH" or user_team == "LSG":
    
    if user_team in team_list:
        other_team_list =[i for i in team_list if i!=user_team]  #--------------this create new list of team and remove user selected team
        print("Other Teams are : ",other_team_list)
#--------------------------------------------------------------------------------------------- 
    opponant_team = random.choice(other_team_list)
    print("Your Team is     : ",user_team)
    print("Opponant Team is : ",opponant_team)
    Toss = True                     #-------------------------------------------means if team selection wrok than toss true otherwise false
else:
    print("-------!!!!!!!!!__INVAILD ___ TEAM _ YOU SELECT____!!!!!!!!!!!!!!!!!!!!!")
    
print("------------------------------------------------------------------------------------------------------------------------")

# ------------------------------------------------------TOSS SELECTION PHASE 2---------------------------------------------------------------
Toss_list=["H","T"]
BB_list=["BATTING","BALLING"]
if Toss:                    # by default it true 
    print("\t:::::::::::::::::::::TOSS TIme::::::::::::::::::::::::::")
    user_Toss=" "
    toss_flag=False
    user_win_Toss=False
    
    while toss_flag!=True:
        user_Toss=input("enter (H/T) :: ").upper()
        if user_Toss =="H" or user_Toss =="T":
            toss_flag=True
            random_Toss=random.choice(Toss_list)
            print("\tYou select : ",user_Toss)
            print("\tActual Toss : ",random_Toss)
            
            if user_Toss == random_Toss:
                user_win_Toss=True #------------------------------------------------------------------------------
                print("\n Ahhhha !!!!!!!!!!! YOU WIN THE TOSS _-----_----------_------")
                print("-------what do you want , Batting or Balling  (BATTING/BALLING)  !!!!!!!!")
                user_select_bb=" "
                bb_choice=False
                while bb_choice!=True:
                    user_select_bb=input("Enter your choice : ").upper()
                    if user_select_bb=="BATTING" or user_select_bb =="BALLING":    
                        print("----Nice ,YOU select  ",user_select_bb)
                        
                        opponant_choice=[i for i in BB_list if i!=user_select_bb] #---------this line and below will automatically select opponent choice and stored it 
                        print("opponant get ",opponant_choice)
                        
                        bb_choice = True
                    else:
                        print("------PLEASE Correct select BATTING OR BALLING ?????????????????  ")
            else:
                print("-------------Ohhhhh????? YOU LOSS THE TOSS")
                opponant_select_BB=random.choice(BB_list)
                print("----Now ,OPPONANT select  ",opponant_select_BB)
                
                
                user_choice=[i for i in BB_list if i!= opponant_select_BB]   # -------------------------this line and below will automaticall select user choice and stored it
                print("You get  ",user_choice)
        else:
            print("Invalid option you select please H or T")
    
else:
    pass
    

# ------------------------------------------------------INNINGS SELECTION PHASE 3---------------------------------------------------------------
if Toss:
    if user_win_Toss:                       #----if user win the toss
        if user_select_bb == "BATTING":
            first_innings = "user"
            second_innings = "opponant"
        else:
            first_innings = "opponant"
            second_innings = "user"
    else:                       # ------------if opponant win the toss
        if opponant_select_BB == "BATTING":
            first_innings = "opponant"
            second_innings = "user"
        else:
            first_innings = "user"
            second_innings = "opponant"
else:
    pass



# ------------------------------------------------------FIRST INNINGS PHASE 4---------------------------------------------------------------
print()
player1_run=0
player1_wicket=0
player1_over=0.0


player2_run=0
player2_wicket=0
player2_over=0.0

opponant_turn=False

print("------------------------------------------------------------------------------------------------------------")
run_list=["1","2","3","0","SIX","FOUR","WHITE_BALL","NO_BALL","WICKET"]

print(":::::::::::::::::::::::::FIRST INNINGS IS STARTED::::::::::::::::::::::::::::::::::::")
if Toss:
    if first_innings == "user":
        print("PRESS Enter to start the match")
        input()
        print("\t\t",user_team," VS ",opponant_team)
        print()
        print("press enter for playin first ball : ")
        input()
        while player1_over!=0.6:
            random_ball = random.choice(run_list)
            
            if random_ball=="1":
                player1_run+=1 
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("!!!!! oh YOU Get only one run keep trying !")
            elif random_ball=="2":
                player1_run+=2
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("!!!Nice you get  2 Runs")
            elif random_ball =="3":
                player1_run+=3
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("!!!!wow, You get 3 Runs , well played_________!")
            elif random_ball=="0":
                player1_run+=0
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("~~~~,This DOT BALL , Tring to play well ~~~~~~~~~~~~~~~~~~~~~~~")
            elif random_ball=="SIX":
                player1_run+=6 
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("$$$___EXcellent Six ! You get Six runs , NICE__")
            elif random_ball=="FOUR":
                player1_run+=4
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("***___Asome, FOUR ! You get Four runs , Well played____")
            elif random_ball=="WHITE_BALL":
                player1_run+=1 
                
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("`````````````WHITE BALL```````````````````````")
            elif random_ball=="NO_BALL":
                player1_run+=1 
                
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("####_NO__BALL######")
            else:
                player1_wicket+=1 
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("???????WHAT ,This is a WICKET, ?????????????????????")
                break
            print("\n\tpress enter for playing next ball")
            input()

        print("\n::::::::::::::::::::::YOUR Final SCORE IS ::::::::::::::::::::::")    
        print(f"\n\t{user_team} :  {player1_run+0}/{player1_wicket}\t({player1_over})")
    else:              #---------------------------------------------------------------------------IF user select balling
        print("PRESS Enter to start the match")
        input()
        print("\t\t",opponant_team," VS ",user_team)
        print()
        
        print("press enter for playin first ball : ")
        input()
        while player2_over!=0.6:
            random_ball = random.choice(run_list)
            
            if random_ball=="1":
                player2_run+=1 
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("!!!!! oh YOU Get only one run keep trying !")
            elif random_ball=="2":
                player2_run+=2
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("!!!Nice you get  2 Runs")
            elif random_ball =="3":
                player2_run+=3
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("!!!!wow, You get 3 Runs , well played_________!")
            elif random_ball=="0":
                player2_run+=0
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("~~~~,This DOT BALL , Tring to play well ~~~~~~~~~~~~~~~~~~~~~~~")
            elif random_ball=="SIX":
                player2_run+=6 
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("$$$___EXcellent Six ! You get Six runs , NICE__")
            elif random_ball=="FOUR":
                player2_run+=4
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("***___Asome, FOUR ! You get Four runs , Well played____")
            elif random_ball=="WHITE_BALL":
                player2_run+=1 
                
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("`````````````WHITE BALL```````````````````````")
            elif random_ball=="NO_BALL":
                player2_run+=1 
                
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("####_NO__BALL######")
            else: 
                player2_wicket+=1 
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("???????WHAT ,This is a WICKET, ?????????????????????")
                break
            print("\n\tpress enter for playing next ball")
            input()
        
        print("\n::::::::::::::::::::::YOUR Final SCORE IS ::::::::::::::::::::::")    
        print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")


# ------------------------------------------------------Second INNINGS PHASE 5---------------------------------------------------------------
print()
print(":::::::::::::::::::::::::SECOND INNINGS IS STARTED::::::::::::::::::::::::::::::::::::")
if Toss:
    if second_innings == "user":
        print("PRESS Enter to start the match")
        input()
        print("\t\t",user_team," VS ",opponant_team)
        print()
        print("press enter for playin first ball : ")
        input()
        while player1_over!=0.6:
            random_ball = random.choice(run_list)
            
            if random_ball=="1":
                player1_run+=1 
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("!!!!! oh YOU Get only one run keep trying !")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball=="2":
                player1_run+=2
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("!!!Nice you get  2 Runs")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball =="3":
                player1_run+=3
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("!!!!wow, You get 3 Runs , well played_________!")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball=="0":
                player1_run+=0
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("~~~~,This DOT BALL , Tring to play well ~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball=="SIX":
                player1_run+=6 
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("$$$___EXcellent Six ! You get Six runs , NICE__")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball=="FOUR":
                player1_run+=4
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("***___Asome, FOUR ! You get Four runs , Well played____")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball=="WHITE_BALL":
                player1_run+=1 
                
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("`````````````WHITE BALL```````````````````````")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            elif random_ball=="NO_BALL":
                player1_run+=1 
                
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("####_NO__BALL######")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
            else:
                player1_wicket+=1 
                player1_over+=0.1
                
                print(f"\n\t{user_team} :  {player1_run}/{player1_wicket}\t({player1_over})")
                print("???????WHAT ,This is a WICKET, ?????????????????????")
                print(f"-----------------------------You want {player2_run-player1_run} runs for winning")
                
                break
            print("\n\tpress enter for playing next ball")
            input()

        print("\n::::::::::::::::::::::YOUR Final SCORE IS ::::::::::::::::::::::")    
        print(f"\n\t{user_team} :  {player1_run+0}/{player1_wicket}\t({player1_over})")
    else:              #---------------------------------------------------------------------------IF user select balling
        print("PRESS Enter to start the match")
        input()
        print("\t\t",opponant_team," VS ",user_team)
        print()
        
        print("press enter for playin first ball : ")
        input()
        while player2_over!=0.6:
            random_ball = random.choice(run_list)
            
            if random_ball=="1":
                player2_run+=1 
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("!!!!! oh YOU Get only one run keep trying !")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball=="2":
                player2_run+=2
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("!!!Nice you get  2 Runs")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball =="3":
                player2_run+=3
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("!!!!wow, You get 3 Runs , well played_________!")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball=="0":
                player2_run+=0
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("~~~~,This DOT BALL , Tring to play well ~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball=="SIX":
                player2_run+=6 
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("$$$___EXcellent Six ! You get Six runs , NICE__")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball=="FOUR":
                player2_run+=4
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("***___Asome, FOUR ! You get Four runs , Well played____")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball=="WHITE_BALL":
                player2_run+=1 
                
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("`````````````WHITE BALL```````````````````````")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            elif random_ball=="NO_BALL":
                player2_run+=1 
                
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("####_NO__BALL######")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
            else:
                player2_wicket+=1 
                player2_over+=0.1
                
                print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")
                print("???????WHAT ,This is a WICKET, ?????????????????????")
                print(f"-----------------------------You want {player1_run-player2_run} runs for winning")
                
                break
            print("\n\tpress enter for playing next ball")
            input()
        
        print("\n::::::::::::::::::::::YOUR Final SCORE IS ::::::::::::::::::::::")    
        print(f"\n\t{opponant_team} :  {player2_run}/{player2_wicket}\t({player2_over})")

# ------------------------------------------------------RESULT PHASE 6---------------------------------------------------------------
if Toss:

    print("\n================ MATCH RESULT ================\n")
    print("------------------------------------------------------------------")
    print(f"\t{user_team}: {player1_run}/{player1_wicket}")
    print("------------------------------------------------------------------")
    print(f"\t{opponant_team}: {player2_run}/{player2_wicket}")
    print("------------------------------------------------------------------")
    

    if player1_run > player2_run:
        print(f"\n{user_team} WON the match!")
    elif player2_run > player1_run:
        print(f"\n{opponant_team} WON the match!")
    else:
        print("Match Tied!")