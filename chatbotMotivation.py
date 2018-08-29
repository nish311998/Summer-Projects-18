import random
inputstatements = ["hey, i am depressed", "cheer me up", "i am sad", "i need some help", "can you console me"]
outputstatements = ["dude you are the best", "it is at the toughest times that you really grow", "one day you will be the most succesful person to live", "keep grinding"]

print("What is up my friend?")
while True:
    userinput = input();
    if userinput.lower() in inputstatements:
        print(random.choice(outputstatements))
    elif userinput.lower() == ("hey" or "hi" or "hello"):
        print("yo")
    elif userinput == ("bye" or "cya"):
        break
    else:
        print("Idk man I am do not know how to respond to that")
   
