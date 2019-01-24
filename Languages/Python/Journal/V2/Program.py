from JAUtilities import *

def main():
    """Main loop for running the program"""
    print("==========================\nWelcome to the journal app\n==========================")
    Continue = True
    while(Continue == True):
        selection = input("\nWhat do?\n(C)reate a jounral (L)oad a Journal: ")
        selection = selection.upper()
        if(selection == "C"):
            newName = input("Jounral Name: ")
            CurrentJournal = Journal(newName)
            Continue = False
        elif(selection == "L"):
            validInput = False
            while validInput == False:
                try:
                    newName = input("What journal would you like to load?")
                    CurrentJournal = loadJournal(newName)
                except:
                    print("Invalid journal")
                else:
                    validInput = True
            Continue = False

        else:
            print("Invalid input")

    Continue = True
    while(Continue == True):
        selection = input("\nWhat do?\n(A)dd an Entry, (L)ist all entries, (E)xit application: ")
        selection = selection.upper()
        if(selection == "E"):
            Continue = False
        elif(selection == "L"):
            CurrentJournal.listEntries()
        elif(selection == "A"):
            CurrentJournal.addEntry()
            CurrentJournal.saveJournal()
        else:
            print("Invalid input")

main()
