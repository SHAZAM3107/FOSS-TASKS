import random

l=["rock","paper","scissors"]# len(l)=2

while 1:# playing infinite games with the pc until we are tired :)
    player=input()# taking the players input as string
    rand_pc=l[random.randrange(2)]# telling the computer to take a random choice every time

    if rand_pc==player:
        print(rand_pc)
        print("draw")# if both end up with same thing the match is draw

    else:

        if player=="rock":
            if rand_pc=="scissors":
                print(rand_pc) # printing what random choice the computer made
                print("player wins")# rock blunts scissors
            elif rand_pc=="paper":
                print(rand_pc)# printing what random choice the computer made
                print("computer wins")# paper covers rock

        if player=="scissors":
            if rand_pc=="paper":
                print(rand_pc)# printing what random choice the computer made
                print("player wins")# scissors cut paper
            elif rand_pc=="rock":
                print(rand_pc)# printing what random choice the computer made
                print("computer wins")# rock blunts scissors

        if player=="paper":
            if rand_pc=="rock":
                print(rand_pc)# printing what random choice the computer made
                print("player wins")# paper covers rock
            elif rand_pc=="scissors":
                print(rand_pc)# printing what random choice the computer made
                print("computer wins")# scissors cut paper
