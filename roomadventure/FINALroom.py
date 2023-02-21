###########################################################################################
# Name: Dr. Jean Gourd
# Date: 2022-01-04
# Description: A basic GUI Room Adventure game to show its mechanics and gameplay.
###########################################################################################

###########################################################################################
# import libraries
from tkinter import *

###########################################################################################
# constants
VERBS = [ "go", "look", "take", "use" ]                    # the supported vocabulary verbs
QUIT_COMMANDS = [ "exit", "quit", "bye" ]           # the supported quit commands

###########################################################################################
# the blueprint for a room

#root = Tk()
#def startgame():
    #turn_off = Button(root, text="START GAME", command=root.destroy)
    #turn_off.pack()
#startgame()
#root.mainloop

class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, image, description, exits (e.g., south), exit locations (e.g., to the
        # south is room n), items (e.g., table), item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []
        self._time = "day"

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, t):
        self._time = t

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table 
    #  Exits: east south 
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "Time: {}\n".format(self.time)
        s += "{}\n".format(self._description)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        return s

###########################################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # a list of rooms will store all of the rooms
        # r1 through r4 are the four rooms in the "mansion"
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        Game.rooms = []
        global r5
        global r4

        # first, create the room instances so that they can be referenced below
        r1 = Room("Room 1", "Room1pic.gif")
        r2 = Room("Room 2", "Stairs.gif")
        r3 = Room("Room 3", "Kitchen.gif")
        r4 = Room("Room 4", "Bathroom.gif")
        r5 = Room("Room 5", "Playroom.gif")
        r6 = Room("Room 6", "room2.gif")


        # room 1
        r1.description = "You look around the room, and see nothing interesting, you should probably explore a little more."
        r1.addExit("east", r4)
        r1.addExit("north", r2)
        r1.addItem("chair", "It is made of wicker. and seems to be higher off the ground than your typical kitchen chair")
        r1.addItem("table", "It is made of oak, and has cat placemats on it")
        r1.addItem("note", "You may be wondering why you are here, well you have been selected to remove a cat from the house. Although this sounds pretty simple the past 27 people to try and do this were killed, so best of luck. P.S. The cat is very active during the day, and he does not like when people go into hed bedroom.")
        Game.rooms.append(r1)

        # room 2
        r2.description = "This room smells funny, and has stairs in the corner, I wonder what they lead to. Also there seems to be a comfy couch in the other corner"
        r2.addExit("south", r1)
        r2.addExit("east", r3)
        r2.addExit("stairs", r5)
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("couch", "Looks very comfy, I could 'use' this to take a nap")
        r2.addItem("stairs", "There are some old beat up wooded stairs in the corner... They seem to once again have lots of scratch marks on them")
        Game.rooms.append(r2)

        # room 3
        r3.description = "Hmmmmmm, this seems like a normal kitchen, nothing suspicious in here."
        r3.addExit("west", r2)
        r3.addExit("south", r4)
        r3.addItem("knives", "The knives do not seem like they have been used, maybe they are brand new")
        r3.addItem("sink", "The sink is dry, and the only thing in it seems to be a bowl with a picture of a cat on it")
        r3.addItem("cabinet" , "The cabinet seems to be scratched up, and when you open them all you see is cat food, and a ball of yarn")
        r3.addItem("note", "There seems to be a note on the counter, it reads: 'Remember to stay away from the cat nip as you are super sensitive to it'")
        Game.rooms.append(r3)

        # room 4
        r4.description = "This is a rather small bathroom, but there is a cool picture on thw wall, I kinda want to go look at it."
        r4.addExit("north", r3)
        r4.addExit("west", r1)
        r4.addItem("toilet", "The toilet is smaller than usual, as if it was meant for a small person or even a animal")
        r4.addItem("painting", "You inspect the painting and it is the same female cat in the picture frame when you first entered. upon closer inspection you realize it moves! behind it is a safe, might want to bring it with you")
        r4.addGrabbable("safe")
        Game.rooms.append(r4)
        
        #Room 5
        r5.describtion = "This seems like a animals play room, very interesting, there are cat toys scattered all over the room"
        r5.addExit("stairs", r2)
        r5.addExit("east", r6)
        r5.addItem("bowl", "in the corner of the room you see a empty cat bowl")
        r5.addItem("katana", "The katana is in a long green sheath, I wonder how much it costed?")
        r5.addItem("bin", "You go over to look in the bin. To your surprise there is just a bunch of cat toys. Just as you are about to walk away you see a piece of paper at the bottom of the bin! You reach down to grab it and it says 'safe_combination'. Might want to take that for later, could be useful.")
        r5.addItem("rug", "You find another rug, but this one is much fluffier, and you can see small imprints in it. The imprints almost look like animal paws... Strange.")
        r5.addItem("painting", "This painting has a picture of what seems to be a male cat. At the bottom you see writting that says 'Master Whiskers'")
        r5.addGrabbable("safe_combination")
        #Room 6
        

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1

        # initialize the player's inventory
        Game.inventory = []

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process() in the class
        # bind the tab key to the function complete() in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")
        #elif (Game.currentRoom == def):
           # Game.img = PhotoImage(file="victory.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now\nis quit.\n You either died because you went up the stairs during the day time, or you went into the cats bedroom")
        #elif (Game.currentRoom == def):
            #Game.text.insert(END, "Congradulations, You beat the game.\n")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
        Game.text.config(state=DISABLED)

        # support for tab completion
        # add the words to support
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables

    # play the game
    def play(self):
        # create the room instances
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus("WELCOME TO ROOM ADVENTURE!")

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)

        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()

            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # set a default response
                    response = "You can't go in that direction."
                    #sets stairs
                    if(noun == "stairs" and Game.currentRoom.time == "day"):
                        if("cat_nip" in r5.items):
                             print("Congradulations, You have beaten the game. When you went back up stairs, you found the cat sleeping next to his bowl, and funny enough there was no cat nip left. It turns out he was super sensitive to it, and it caused him to fall asleep while he was out playing during the day.\n\n The cat was succefully removed from the house and released into the wild where he is thriving.")
                             exit(0)
                        else:
                            Game.currentRoom = None
                            response = "As you walked up the stairs, you start to hear running, and right as you get to the top you see a cat flying towards you, but before you can react the cat side kicked you down the stairs! Sadly from this fall you broke you neck and died:(. Restart and try again."
                    elif(noun == "east" and Game.currentRoom.name == "Room 5"):
                        Game.currentRoom = None

                    # check if the noun is a valid exit
                    elif (noun in Game.currentRoom.exits):
                        # get its index
                        i = Game.currentRoom.exits.index(noun)
                        # change the current room to the one that is associated with the specified exit
                        temp = Game.currentRoom.time
                        Game.currentRoom = Game.currentRoom.exitLocations[i]
                        Game.currentRoom.time = temp
                        # set the response (success)
                    response = "You walk {} and enter another room.".format(noun)
                # the verb is: look
                elif (verb == "look"):
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid item
                    if (noun in Game.currentRoom.items):
                        # get its index
                        i = Game.currentRoom.items.index(noun)
                        # set the response to the item's description
                        response = Game.currentRoom.itemDescriptions[i]
                # the verb is: take
                elif (verb == "take"):
                    # set a default response
                    response = "You don't see that item."
                    if (noun == "safe" and Game.currentRoom.name == "Room 4" and "safe" not in Game.inventory):
                        r4.itemDescriptions.remove("You inspect the painting and it is the same female cat in the picture frame when you first entered. upon closer inspection you realize it moves! behind it is a safe, might want to bring it with you")
                        r4.items.remove("painting")
                        r4.addItem("painting","You inspect the painting and see it is the same femal cat from when you first entered, owever it is pushed to the side, and has a empty hole behind where the safe use to be")
                    if (noun == "safe_combination" and Game.currentRoom.name == "Room 5" and "safe_combination" not in Game.inventory):
                        r5.itemDescriptions.remove("You go over to look in the bin. To your surprise there is just a bunch of cat toys. Just as you are about to walk away you see a piece of paper at the bottom of the bin! You reach down to grab it and it says 'safe_combination'. Might want to take that for later, could be useful.")
                        r5.items.remove("bin")
                        r5.addItem("bin","You go over and look into the bin where you found the safe combination. Unlike last time, there is just cat toys in it")

                    # check if the noun is a valid grabbable and is also not already in inventory
                    if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                        # get its index
                        i = Game.currentRoom.grabbables.index(noun)
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(Game.currentRoom.grabbables[i])
                        # set the response (success)
                        response = "You take {}.".format(noun)
                        
                elif (verb == "use"):
                    #set default response
                    response = "I do not have that item"
                    #using the couch
                    if (noun == "couch"):
                        response = "There is no couch in the room"
                        if (Game.currentRoom.name == "Room 2"):
                            response = "You end up taking a nap and 12 hours end up passing"
                            if (Game.currentRoom.time == "day"):
                                Game.currentRoom.time = "night"
                            else:
                                Game.currentRoom.time = "day"
                    #describes using the safe
                    elif noun in Game.inventory:
                        if (noun == "safe"):
                            # set the response to the item's
                            #  description
                            if ("safe_combination" in Game.inventory):
                                response = "congratulations you opened the safe, you have recieved a new Item, Cat Nip!"
                                Game.inventory.append("cat_nip")
                                Game.inventory.remove("safe")
                            else:
                                response = "Hmmm, I dont know the code, maybe it is written down somewhere"
                    #Describes Cat_Nip
                        elif(noun == "cat_nip"):
                            if (Game.currentRoom.name == "Room 5"):
                                Game.inventory.remove("cat_nip")
                                r5.addItem("cat_nip", "We have place the cat_nip in the food bowl")
                                r5.addGrabbable("catnip")
                                response = "You have decided to put the cat_nip in the food bowl, guess we will have to try and come back during the day to see what happened"
                            else:
                                response = "Hmmmmm, we should probably put this is a different room"
                        #describes what heppens when you use safe combination
                        elif(noun == "safe_combination"):
                            if ("safe_combination" in Game.inventory):
                                response = "The combination is 'Hi Professor Gourd', now use the safe and open it"
                            else:
                                response = "I don't have that item."
                
                    
                    

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

    # implements tab completion in the Entry widget
    def complete(self, event):
        # get user input and the last word of input
        words = Game.player_input.get().split()
        # continue only if there are words in the user's input
        if (len(words)):
            last_word = words[-1]
            # check if the last word of input is part of a valid verb/noun
            results = [ x for x in Game.words if x.startswith(last_word) ]

            # initially, there is no matching verb/noun
            match = None

            # is there only a single valid verb/noun?
            if (len(results) == 1):
                # the result is a match
                match = results[0]
            # are there multiple valid verbs/nouns?
            elif (len(results) > 1):
                # find the longest starting substring of all verbs/nouns
                for i in range(1, len(min(results, key=len)) + 1):
                    # get the current substring
                    match = results[0][:i]
                    # find all matches
                    matches = [ x for x in results if x.startswith(match) ]
                    # if there are less matches than verbs/nouns
                    if (len(matches) != len(results)):
                        # go back to the previous substring
                        match = match[:-1]
                        # stop checking
                        break
            # if a match exists, replace the user's input
            if (match):
                # clear user input
                Game.player_input.delete(0, END)
                # add all but the last (matched) verb/noun
                for word in words[:-1]:
                    Game.player_input.insert(END, "{} ".format(word))
                # add the match
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

        # prevents the tab key from highlighting the text in the Entry widget
        return "break"

###########################################################################################
# START THE GAME!!!
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()

