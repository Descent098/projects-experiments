

class journal:
    """A class that can be instantiated to create a journal"""
    import os

    def __init__(self, name):
        self.name = name

    def load(name):
        # TODO: populate from file if exists
        return []

    def save(name, journal_data):
        # TODO: Write function
        filedir = os.path.abspath(os.path.join(".", "journals" + name + ".jrl"))

        print("Saving to {}".format(filedir))
        fileOutput = open(filename, 'w')

        for entry in journal_data:
            fileOutput.write(entry + "\n")

        fileOutput.close()
