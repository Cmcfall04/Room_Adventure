from Room import Room
######################################################
# creates the rooms
def createRooms():
# r1 through r4 are the four rooms in the mansion
# currentRoom is the room the player is currently in (which
# can be one of r1 through r4)
# since it needs to be changed in the main part of the
# program, it must be global
    global currentRoom
    global r5
    global r1
    global r4
    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")
    r6 = Room("Room 6")
    # add exits to room 1
    r1.addExit("east", r4)
    r1.addExit("north", r2)
    # add items to room 1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it, and it has scratch marks all over it")
    r1.addItem("table", "It is made of oak, It is also all scratched up, and has a picture frame of a beautiful female cat on it")
    # add exits to room 2
    r2.addExit("south", r1)
    r2.addExit("east", r3)
    r2.addExit("stairs", r5)
    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("couch", "Looks very comfy, I could 'use' this to take a nap")
    r2.addItem("stairs", "There are some old beat up wooded stairs in the corner... They seem to once again have lots of scratch marks on them")
    # set room 1 as the current room at the beginning
    #add exit to room 3
    r3.addExit("west", r2)
    r3.addExit("south", r4)
    #add item in room 3
    r3.addItem("knives", "The knives do not seem like they have been used, maybe they are brand new")
    r3.addItem("sink", "The sink is dry, and the only thing in it seems to be a bowl with a picture of a cat on it")
    r3.addItem("cabinet" , "The cabinet seems to be scratched up, and when you open them all you see is cat food, and a ball of yarn")
    r3.addItem("note", "There seems to be a note on the counter, it reads: 'Remember to stay away from the cat nip honey'")
    #add exit for room 4
    r4.addExit("north", r3)
    r4.addExit("west", r1)
    #add item in room 4
    r4.addItem("toilet", "The toilet is smaller than usual, as if it was meant for a small person or even a animal")
    r4.addItem("painting", "You inspect the painting and it is the same female cat in the picture frame when you first entered. upon closer inspection you realize it moves! behind it is a safe, might want to bring it with you")
    #add grabable in room 4
    r4.addGrabbable("safe")
    #add exit in room 5
    r5.addExit("stairs", r2)
    r5.addExit("east", r6)
    #add item to room 5
    r5.addItem("bowl", "in the corner of the room you see a empty cat bowl")
    r5.addItem("katana", "The katana is in a long green sheath, I wonder how much it costed?")
    r5.addItem("bin", "You go over to look in the bin. To your surprise there is just a bunch of cat toys. Just as you are about to walk away you see a piece of paper at the bottom of the bin! You reach down to grab it and it says 'safe_combination'. Might want to take that for later, could be useful.")
    r5.addItem("rug", "You find another rug, but this one is much fluffier, and you can see small imprints in it. The imprints almost look like animal paws... Strange.")
    r5.addItem("painting", "This painting has a picture of what seems to be a male cat. At the bottom you see writting that says 'Master Whiskers'")
    #add grabable to room 5
    r5.addGrabbable("safe_combination")
    #add exit to room 6
    r6.addExit("west", r5)
    # of the game
    currentRoom = r1

def death():

    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$"* 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 +"u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 +"u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3+ "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" +"$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u"+ "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3+ " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9+ "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " *4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 +"u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" *2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2+ " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" +"$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" +"$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")

######################################################
# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game
# play forever (well, at least until the player dies or asks to
#  quit)
#requires user to type enter to begin
print("Hello Kung Fu Master!, you have been brought here today to complete the task of removing the other Kung Fu Master named Master Wiskers from the house. He has been terrorizing those who have tried to move into this house for the past decade. Many have failed at trying to do this, and you are are last hope. Once you remove him from the house, the house will be all yours GOOD LUCK! your gonna need it. (Some hints: He likes to play during the day so you best way to get him is duirng the night, He has never lost a fight so try to find his weakness)")
Start_Game = input("\nIf you are ready type 'Enter' to enter the house and begin: ")
Start_Game = Start_Game.lower()
if Start_Game == "enter":
    while (True):
        #instant death for entering room 6
        if (currentRoom.name == "Room 6"):
            death()
            print("As soon as you opend the door an alarm sounded, before you could figure out what is going on you hear a loud 'MEOOOOW' and then you were kicked out of the window and killed. Restart to try again")
            break
        # set the status so the player has situational awareness
        # the status has room and inventory information
        status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (currentRoom == None):
            status = "You are dead."

        # display the status
        print("=========================================")
        print(status)
 
        # if the current room is None (and the player is dead),
        #  exit the game
        if (currentRoom == None):
            death()
            break

        # prompt for player input
        # the game supports a simple language of <verb> <noun>
        # valid verbs are go, look, and take
        # valid nouns depend on the verb
        action = input("What to do? ")

        # set the user's input to lowercase to make it easier to
        #  compare the verb and noun to known values
        action = action.lower()

        # exit the game if the player wants to leave (supports
        #  quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye"):
            break

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use"
        # split the user input into words (words are separated by
        #  spaces)
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."
                #sets death if you go up stairs during day time
                if(noun == "stairs"):
                    if(currentRoom.time == "day"):
                        if("cat_nip" in r5.items):
                           print("Congratulations!, you have beat the game. When you came up the stairs you found a cat passed out in the ground next to the bowl of cat nip! you decide to take the cat outside and the second you stepped outside the authorities cheered and congratulated you. It turns out that cat was actaully Mr.Wiskers and he had been beating up anyone who came into his home, and crazy enough even killed some. However it tuns out he had a extreme sensitivity to cat nip and passed out as soon as he took a bite of the little bit you placed in the bowl. In the end you recieved the house for free and Mr.Wiskers was relocated into the wild on the other side of the world, where as of now I have heard he became the king of the jungle!")
                           break
                        else:
                            death()
                            print("As you walked up the stairs, you start to hear running, and right as you get to the top you see a cat flying towards you, but before you can react the cat side kicked you down the stairs! Sadly from this fall you broke you neck and died:(. Restart and try again.")
                            break
                  
                # check for valid exits in the current room        
                
                for i in range(len(currentRoom.exits)):
                    # a valid exit is found
                    if (noun == currentRoom.exits[i]):
                        # change the current room to the one
                        #  that is associated with the specified
                        #  exit
                        temp = currentRoom.time
                        currentRoom =  currentRoom.exitLocations[i]
                        currentRoom.time = temp

                        # set the response (success)
                        response = "Room changed."

                        # no need to check any more exits
                        break
                    
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                for i in range(len(currentRoom.items)):
                    # a valid item is found
                    if (noun == currentRoom.items[i]):
                        # set the response to the item's
                        #  description
                        response = currentRoom.itemDescriptions[i]

                        # no need to check any more items
                        break
            #The verb is use
            #Created a use function
            elif (verb == "use"):
                # set a default response
                response = "I don't have that item."

                # check for valid items in the current room
                #describes what happens when you use the couch
                if (noun == "couch"):
                    response = "There is no couch in the room"
                    if (currentRoom.name == "Room 2"):
                        response = "You end up taking a nap and 12 hours end up passing"
                        if (currentRoom.time == "day"):
                            currentRoom.time = "night"
                        else:
                            currentRoom.time = "day"
                #describes what happens when you use safe
                elif noun in inventory:
                    if (noun == "safe"):
                        # set the response to the item's
                        #  description
                        if ("safe_combination" in inventory):
                            response = "congratulations you opened the safe, you have recieved a new Item, Cat Nip!"
                            inventory.append("cat_nip")
                            inventory.remove("safe")
            
                        else:
                            response = "Hmmm, I dont know the code, maybe it is written down somewhere"
                    #describes what happens when you use cat nip
                    elif(noun == "cat_nip"):
                        if (currentRoom.name == "Room 5"):
                            inventory.remove("cat_nip")
                            r5.addItem("cat_nip", "We have place the cat_nip in the food bowl")
                            r5.addGrabbable("cat_nip")
                            response = "You have decided to put the cat_nip in the food bowl, guess we will have to try and come back during the day to see what happened"
                        else:
                            response = "Hmmmmm, we should probably put this is a different room"
                    #describes what heppens when you use safe combination
                    elif(noun == "safe_combination"):
                        if ("safe_combination" in inventory):
                            response = "The combination is 'Hi Lori', now use the safe and open it"
                        else:
                            response = "I don't have that item."

                        # no need to check any more items
                    
                
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."

                # check for valid grabbable items in the current
                #  room
                for grabbable in currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable): 
                        # add the grabbable item to the player's
                        #  inventory
                        inventory.append(grabbable)

                        # remove the grabbable item from the
                        #  room
                        currentRoom.delGrabbable(grabbable)

                        # set the response (success)
                        response = "Item grabbed."

                        # no need to check any more grabbable
                        #  items
                        break

        # display the response
        print("\n{}".format(response))
