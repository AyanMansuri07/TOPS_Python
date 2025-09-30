import random
print("---------------------------------------------WELECOM--TO--THE--GAME---------------------------------------------")


main_list =[]

for i in range(1,13):
    main_random = random.randint(1,100)
    while main_random in main_list:      # ----------------------for append all number in uniquely
        main_random = random.randint(1,100)
    main_list.append(main_random)
print(main_list)   # -------------this is print in list form

player1_list = main_list[:6]  #----------------------
player2_list =main_list[6:]   #----------------------

print("player 1 :: ",player1_list) #---------player 1
print("player 2 :: ",player2_list) #---------player 2


while player2_list!=[] or player1_list!=[]:

    print("press enter key for ......") #--------------------- Enter key 
    input()
    number = random.choice(main_list)   # pic the random number from the main list 
    print("number :: ",number)

    if number in player1_list:
        print("player 1 has ",number)
        player1_list.remove(number)
    elif number in player2_list:
        print("player 2 has ",number)
        player2_list.remove(number)
    else:
        pass     
    print("player 1 :: ",player1_list)
    print("player 2 :: ",player2_list)
    
    if player1_list == []:
        print("\n\t::::::::::::!!!!!!!!!!!!____Player 1 WIN THE GAME !!!!!!!!!!!!!!")
        break
    elif player2_list ==[]:
        print("\n\t::::::::::::!!!!!!!!!!!!____Player 2 WIN THE GAME !!!!!!!!!!!!!!")
        break
