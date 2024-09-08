def marriage(a):
    if a == "yes":
        print("Congratulation!! You marry to the Queen and live a peaceful and lovely life.")
        print("You won!!")
        quit()
    elif a == "no":
        print("Are you crazy to reject the proposal from the Queen!!!")
        print("Soon after rejection the Queen orders her guard to execute you.")
        print("GOODBYE, YOU DIE!!!")
    else:
        quit()

def bridge(a):
    if a == "swim":
        print("you try to cross the river by swimming, but oops! didn't I tell there is an aligator in that river.")
        print("Sorry, YOU DIE!!!!")
        quit()
    elif a == "boat":
        print("Good Choice!!, you successfully cross the river and end up in a village.")
        print("The Queen of that falls in love with you and wants to marry you!")
        opt = input("What is your answer to the Queen, is Yes/No? ").lower()
        marriage(opt)
    else:
        quit()

def Right(a):
    if a == 1:
        print("You talk to the witch. She again gives you chance whether to choose the princess route or accept her gift.")
        opt = input("What would you choose 0/1? ")
        if opt.isdigit():
            opt = int(opt)
        else:
            quit()
        
        if opt == 0 :
            print("You really thought choosing princess would be a better idea, sorry my friend she is a monster.")
            print("YOU DIE!!!")
            quit()
        elif opt == 1:
            print("The special gift recieved from the witch is superpower which make the hero of the village")
            print("YOU WIN!!!")
            quit()
    elif a == 2:
        print("You really thought choosing princess would be a better idea, sorry my friend she is a monster.")
        print("YOU DIE!!!")
        quit()


print("Hello, Welcome to my game!!")
opt = input("Enter 'start' to start the game: ")
if opt == "start":
    print("You are given two choices:")
    print("1. Go RIGHT")
    print("2. Go LEFT")
    option = input("Tell your choice: ")
    if option.isdigit():
        option = int(option)
    else:
        quit()
    if option == 1:
        print("You are given two choices:")
        print("1. Talk to witch")
        print("2. Talk to princess")
        options = input("Tell your choice: ")
        if options.isdigit():
            options = int(options)
        else:
            quit()
        Right(options)
    elif option == 2:
        print("You reach to a river")
        print("You are given two choices:")
        print("1. Swim across the river")
        print("2. Use a boat to travel the river")
        opti = input("Tell your choice: ")
        if opti.isdigit():
            opti = int(opti)
        else:
            quit()
        bridge(opti)