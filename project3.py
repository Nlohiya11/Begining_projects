print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choose1 = input("Which direction you choose? Left or Right\n")
direction = choose1.lower()
if direction == "left":
    print("now you can see a lake in front of you")
    choose2 = input("What will you do? swim or wait\n ")
    swim = choose2.lower()
    if swim == "wait":
        print("Their is 3 boat have 3 colors")
        choose3 = input("you have to choose one color. red/black/blue\n")
        color = choose3.lower()
        if color == "blue":
            print("you find the treasure")
        else:
            print("you went into a pirate boat.\n *GAME OVER*  ")
    else:
        print("Crocodile ate you\n *GAME OVER*  ")
else:
    print("Your went into desert\n *GAME OVER*  ")
