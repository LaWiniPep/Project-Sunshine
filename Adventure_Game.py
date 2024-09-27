

def main():
    """
    Start Game
    Make Choice from given values
    return result from choice
    runs until finished
    """
    currentNode="start"
    
    print(game[currentNode][0])
    print(game[currentNode][1])
    print(game[currentNode][3])
    input("Pick one (1/2) > " )
    if input==1:
        currentNode.update(currentNode[2])
    else:
        currentNode.update(currentNode[3])
    print(currentNode)


def getGame():
    """
    Dictionary containing game objective
    """
game={    
    "start": ["You wake up to your cat, Pepper, riding your dog, Lafayette, like a horse out of the bedroom and heading towards the living room.", "1) Go back to bed. Obviously you are dreaming.", "sleep", "2) Get out of bed and investigate what is going on.", "wake"], 
    "sleep": ["A sudden crash outside the bedroom wakes you up again.", "1) Go and investigate the noise.", "wake2", "2) Go back to bed. That’s a tomorrow problem.", "quit"], 
    "wake": ["As you walk into the living room you notice a trail of spiders leading into your kitchen.", "1) Oh heck no! I'm going back to bed!", "quit", "2) Follow the spiders into the Kitchen.", "invesitgate"], 
    "wake2": ["When you walk outside the bedroom you see what looks to be giant balls of cotton.", "1) Check out the giant balls of white cotton.", "cotton", "2) Call the cops.", "cops"], 
    "invesitgate": ["Inside the kitchen you see the spiders have interconnected into one giant organism and are heating up a giant pot.", "1) Grab the shotgun off the wall and unload on the monstrosity.", "shotgun", "2) Run out of the house and pour gasoline on your problems.", "gas"], 
    "cotton": ["As you get close to the giants balls of cotton you realize they are sticky. When you check Inside you see Pepper and Lafayette are alive, but seem to be in a comatose state.", "1) Grab them and run out of the house!", "run", "2) Go back to bed. Things are getting to real.", "quit"], 
    "cops": ["When you call 911 they laugh at you and ask if you have been drinking tonight.", "1) Yell at them tell them to send someone and  hang up.", "endCall", "2) Tell them you had been under the influence. And that you're going back to bed.", "quit"], 
    "shotgun": ["The spiders dismantle and charge at you.", "1) Keep firing! Only good spider is a dead one.", "shoot", "2) Bail!!!!", "bail"], 
    "gas": ["Just before you strike the match you seethrough your front window Pepper riding Lafayette away from the spiders and towards you.", "1) Grab a rock and smash the window.", "smash", "2) Open the door and run back in for them.", "goBack"], 
    "run": ["As you run out of the house with your two balls of fluff in tow you see a giant black shadow coming after you. Its millions of spiders connected to create a mega organism.", "1) Run out the front door and keep running until you collapse", "collapse", "2) Stand your ground and fight.", "fight"], 
    "endcall": ["You wait outside for the cops to show up, but they never do. A shadow is casted over you. You look up. The spiders have found you. They collapse on top of you. Bringing you to and endless darkness.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
    "shoot": ["As you keep firing  you run out of ammo. The sound has disoriented the remaining spiders. You notice that one of the shots spread alcohol all over the floor infront of you.", "1) Set it on fire.", "fire", "2) Grab Pepper and Lafayette and run out the door.", "run2"], 
    "bail": ["As you run out you see Lafayette and Pepper in the corner of the room.", "1) Grab them and run out the door.", "run2", "2) EVERYONE FOR THEMSELVES", "bailHard"], 
    "smash": ["As you smash the window, Pepper kicks Lafayette with her hind legs and he jumps out the window.", "1) You run together outside as far as you can until you collapse from exhaustion.", "collapse", "2) Wait outside your house and hope someone heard everything and called the cops.", "help"], 
    "goBack": ["When you run inside Pepper and Lafayette rush out. As you follow them something grips you from behind and pulls you back in. You are surrounded by spiders. They surround you and you succomb to darkness.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
    "collapse": ["You wake up to Pepper standing on top of you and Lafayette licking your face. You are safe. But your house? It is now spider property.", "1) You win! Try again?", "start", "2) You win! Escape this nightmare??", "quit2"], 
    "fight": ["You fight the spiders with all your might but they are too many. They completely cover you. All you see is darkness. Slowly, you fade away.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
    "fire": ["The fire ignites and the screams of the spiders sends a shiver down your spine. You grab your fire extinguisher and put out the fire. The spiders are dead.", "1) YOU WIN!! Play again?", "start", "2) YOU WIN!! Leave this nightmare?", "quit2"], 
    "run2": ["You frantically try and grab Pepper and Lafayette, but they bolt away. You chase after them but they were too quick. As you look behind you the spiders are closing in. You thrust the window open but as you try and jump out you feel something grab you. As the spiders pull you back to the kitchen the last thing you see before sucumbing to darkness is Pepper and Lafayette jumping out the window.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
    "bailHard": ["You rip the door open and attempt to flee. But the Spiders grab you. As you are getting pulled back you see Pepper and Lafayette run out the door to safety. Too bad the same cant be said for you.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
    "help1": ["As you wait for help you feel a tap on you shoulder. You turn around. The Spider comglomerant is behind you. They drag you back in the house and you are never seen again.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
    "quit1": ["You wake up securly fastened to the wall by a sticky thread. A shadow drops from the corner of the room. It drops down and comes toward you. It looks like a spider the size of a dishwasher. As it gets closer you see it is a mass of spiders collectivly acting as one. It gets close to you. The last thing you see before your eternal darkness is thousands of spiders ready to feed.", "1) You lose. Try again?", "start", "2) You lose. Want to quit?", "quit2"], 
 }


def playNode(node):
    """
    Take node string
    process player input
    return next node
    """
#    keepGoing=True
#    while(keepGoing)
        

main()





