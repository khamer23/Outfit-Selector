###Enter your own sneakers, tops and bottoms and this program will pick out a fit for you

from datetime import datetime
import random

name = input("Enter your name: ")
print("Hi ", name)

#prints current date and time
now = datetime.now()
print("It is: ", now)


while 1:
    print("Let's pick some sneakers!")
    #Takes 3 pairs of sneakers as input and creates a list called sneaker_list with them
    sneaker_1 = input("Sneaker 1: ")
    sneaker_2 = input("Sneaker 2: ")
    sneaker_3 = input("Sneaker 3: ")
    sneaker_list = [sneaker_1, sneaker_2, sneaker_3]
    print("Good kicks!")
    #print(sneaker_list)

    print("Pick 3 tops.")
    #Takes 3 tops as input and creates a list called clothes_tops with them
    top_1 = input("Clothing top 1: ")
    top_2 = input("CLothing top 2: ")
    top_3 = input("Clothing top 3: ")
    clothes_tops = [top_1, top_2, top_3]
    print("Nice pieces!")
    #print(clothes_tops)

    print("Pick 3 bottoms.")
    #Takes 3 bottoms as input and creates a list called clothes_bottoms with them
    bottom_1 = input("Clothing bottom 1: ")
    bottom_2 = input("Clothing bottom 2: ")
    bottom_3 = input("Clothing bottom 3: ")
    clothes_bottoms = [bottom_1, bottom_2, bottom_3]
    print("Great bottoms!")
    #print(clothes_bottoms)
    break

def pick_a_kick():
    #If user wants to add more than 3 sneakers, they can add up to 5 total
    add_four = input("Want to add more sneakers? (Y/N): ")
    if add_four == "Y":
        sneaker_4 = input("Sneaker 4: ")
        sneaker_list.append(sneaker_4)
        add_five = input("Want to add more sneakers? (Y/N): ")
        if add_five == "Y":
            sneaker_5 = input("Sneaker 5: ")
            sneaker_list.append(sneaker_5)
            #print("Wear", random.choice(sneaker_list))
        elif add_five == "N":
            #print("Wear", random.choice(sneaker_list))
            pass
        else:
            print("Error. Try again.")
            retry_five = input("Enter Y/N: ")
            if retry_five == "Y":
                retry_5 = input("Sneaker 5: ")
                sneaker_list.append(retry_5)
                #print("Wear", random.choice(sneaker_list))
            elif retry_five == "N":
                #print("Wear", random.choice(sneaker_list))
                pass
            else:
                print("Error.")
                pick_a_kick()
    elif add_four == "N":
        #print("Wear", random.choice(sneaker_list))
        pass
    else:
        print("Error. Try again.")
        pick_a_kick()
        
def pick_tops():
    #If user wants to add more than 3 tops, they can add up to 5 total
    add_top_4 = input("Want to add more tops? (Y/N): ")
    if add_top_4 == "Y":
        top_4 = input("Clothing top 4: ")
        clothes_tops.append(top_4)
        add_top_5 = input("Want to add more tops? (Y/N): ")
        if add_top_5 == "Y":
            top_5 = input("Clothing top 5: ")
            clothes_tops.append(top_5)
            #print("Wear", random.choice(clothes_tops))
        elif add_top_5 == "N":
            #print("Wear", random.choice(clothes_tops))
            pass
        else:
            print("Error. Try again.")
            try_clothes5 = input("Enter Y/N: ")
            if try_clothes5 == "Y":
                try_clothes_five = input("Clothing top 5: ")
                clothes_tops.append(try_clothes_five)
                #print("Wear", random.choice(clothes_tops))
            elif try_clothes5 == "N":
                #print("Wear", random.choice(clothes_tops))
                pass
            else:
                print("Error.")
                pick_tops()     
    elif add_top_4 == "N":
        #print("Wear", random.choice(clothes_tops))
        pass
    else:
        print("Error. Try again.")
        pick_tops()

def pick_bottoms():
    #If user wants to add more than 3 bottoms, they can add up to 5 total
    add_bottom_4 = input("Want to add more bottoms? (Y/N): ")
    if add_bottom_4 == "Y":
        bottom_4 = input("Clothing bottom 4: ")
        clothes_bottoms.append(bottom_4)
        add_bottom_5 = input("Want to add more bottoms? (Y/N): ")
        if add_bottom_5 == "Y":
            bottom_5 = input("Clothing bottom 5: ")
            clothes_bottoms.append(bottom_5)
            #print("Wear", random.choice(clothes_bottoms))
        elif add_bottom_5 == "N":
            #print("Wear", random.choice(clothes_bottoms))
            pass
        else:
            print("Error. Try again.")
            try_bottoms5 = input("Enter Y/N: ")
            if try_bottoms5 == "Y":
                try_bottoms_five = input("Clothing bottom 5: ")
                clothes_bottoms.append(try_bottoms_five)
                #print("Wear", random.choice(clothes_bottoms))
            elif try_bottoms5 == "N":
                #print("Wear", random.choice(clothes_bottoms))
                pass
            else:
                print("Error.")
                pick_bottoms()         
    elif add_bottom_4 == "N":
        #print("Wear", random.choice(clothes_bottoms))
        pass
    else:
        print("Error. Try again.")
        pick_bottoms()

pick_a_kick()
pick_tops()
pick_bottoms()


print("Wear", random.choice(sneaker_list), "with", random.choice(clothes_tops), "and", random.choice(clothes_bottoms))

