print("Welcome to Teasure Island.")
print("Your mission is to find the treasure.")

lr=input("left or right ? ")
lr=lr.lower()

if lr == "left":
    sw=input("swim or wait ? ")
    sw=sw.lower()
    if sw == "wait":
        wd=input("Red , Blue or Yellow ? ")
        wd=wd.lower()
        if wd == "red":
            print("Burned to Death\nGame Over")
        elif wd == "blue":
            print("Eaten by Snakes\nGame Over")
        elif wd == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Boat sank\nGame Over")
else:
    print("Fall into a hole\nGame Over")

