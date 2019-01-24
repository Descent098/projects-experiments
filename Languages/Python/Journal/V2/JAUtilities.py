from datetime import date #Used to date journal Entries
import pickle #used for object serialization

def loadJournal(title):
    savefile = open('{}.jf'.format(title), 'rb')
    returningJournal = pickle.load(savefile)
    savefile.close()
    return returningJournal


class Journal:
    def __init__(self, name, entries = None):
        """Class constructor, takes the name of the Journal
        as a string, and Journal entries as a list; if there
        are no entries passed then it creates an empty list"""
        self.name = name
        if entries == None:
            self.entries = []
        else:
            self.entries = entries

    def __str__(self):
        """Setting string variable to return the Journl name"""
        return self.name

    def listEntries(self):
        """Returns the entries in the Journal instance in reverse-chronological order"""
        print("listEntries:\n{}".format(self.entries))
        pass

    def printEntry(self, title):
        print(self.entries[0])
        pass

    def saveJournal(self):
        """Saves the Journal out to a file"""
        print("saveJournal")
        savefile = open('{}.jf'.format(self.name), 'wb')
        pickle.dump(self, savefile)
        savefile.close()
        pass

    def addEntry(self):
        """Takes the entries as an argument and appends to
        The instance entries list"""
        entryTitle = input("Give your entry a title: ")
        entryContent = input("What's on your mind?: ")
        newEntry = Entry(entryTitle, entryContent)
        self.entries.append(newEntry)
        print("added Entry{}".format(newEntry))
        self.saveJournal()
        pass



class Entry:

    def __init__(self, Title, Content):
        """Constructor for the class, requires a Ttile
        for the entry as well as some content"""
        self.title = Title
        self.content = Content
        self.date = date.today()

    def __str__(self):
        """Sets string variable for the class to entry title"""
        stringOutput = "{}; {}, added: {}".format(self.title, self.content,self.date)
        return stringOutput

    def __repr__(self):
        """Sets string variable for the class to entry title"""
        stringOutput = "{}; {}, added: {}".format(self.title, self.content,self.date)
        return stringOutput
