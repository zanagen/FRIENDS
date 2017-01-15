def load():
    file = open('Names&Interests', 'r')
    for line in file:
        newLine = line.split("; ")
        newLine[-1] = newLine[-1][:-1]
        interests = newLine[1].split(", ")
        friendDict[newLine[0]] = interests
    file.close()

def endProgram(name):
    file = open('Names&Interests', 'w')
    sentence = ""
    for item in friendDict.keys():
        print(friendDict.keys())
        sentence = sentence + item + "; "
        for i in friendDict[item]:
            sentence = sentence + i + ", "
        sentence = sentence[:-2]
        sentence += "\n"
        print(sentence)
    file.write(sentence)
    file.close()

def start():
    mainP = input("What is your name? ")
    interests = input("Name a few of your interests: ")
    inter = interests.split(", ")
    friendDict[mainP] = inter
    return mainP

def find(name):
    for item in friendDict[name]:
        for part in friendDict.keys():
            if item in friendDict[part] and part != name:
                print(part + ": " + item)

def main():
    quit = True
    load()
    mainP = start()
    while (quit):
        command = input("What would you like to do? ")
        if command == "help":
            print(commands)
        elif command == "find":
            find(mainP)
        elif command == "quit":
            endProgram(mainP)
            print("Thank you for using the FindMeFriends!")
            quit = False

friendDict = {}
commands = ["find", "help", "quit"]
main()