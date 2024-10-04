import json

"""
    textAdventureEditor.py
    complete text adventure editor
    include node editor
    save and load in json format
    """

def main():
    """
    Run main loop
    Calls a menu
    Sends control to other parts of the program
    Handle invalid input
    """
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        userChoice=getMenuChoice()
        
        if userChoice=="0":
            keepGoing = False
        elif userChoice=="1":
            print("Load Default Game")
            game = getDefaultGame()
            
        elif userChoice=="2":
            print("Load a Game File")
            game = loadGame()
            
        elif userChoice=="3":
            print("Save the Current Game")
            game = saveGame()
            
        elif userChoice=="4":
            print("Edit or Add a Node")
            game = editNode()
            
        elif userChoice=="5":
            print("Play the Current Game")
            game = playGame()
            
        else:
            print("You need to follow directions")


def getMenuChoice():
    """
    Prints a menu of user options
    returns a menu choice
    """
    print("Please pick a number 0 throgh 5")
    print("0.) Exit")
    print("1.) Load Defualt Game")
    print("2.) Load a Game File")
    print("3.) Save the Current Game")
    print("4.) Edit or Add a Node")
    print("5.) Play the Current Game")
    userChoice=input("What will you do?  ")
    
    return userChoice
    
    
def getDefaultGame():
    """
    create a single-node default game
    returns the data structure
    """
    game = {
    "start": [
        "Do you want to win or lose?",
        "I want to win",
        "win",
        "I'd rather lose",
        "quit"]
    }

    return game
    
def playGame(game):
    """
    plays the game
    keeps going until next node is quit
    """
    
    currentNode="start"
    keepGoing=True
    while keepGoing:
        if currentNode == "quit":
            keepGoing=False
        else:
            currentNode = playNode(currentNode)
    
    
    
def playNode(game, currentNode):
    """
    given the game data and node
    plays out the node
    returns the next node
    """
    if currentNodeKey in game.keys():
        currentNode = game[currentNode]
        (desc, menuA, nodeA, menuB, nodeB) = currentNode
        print(f"""
        {desc}
        1) {menuA}
        2) {menuB}
        """)
        userChoice = input("Which do you choose (1/2) ")
        if userChoice == "1":
            nextNode = nodeA
        elif userChoice == "2":
            nextNode = nodeB
        else:
            print("That wasn't a choice")
            nextNode = "quit"
        
        return nextNode

main()

