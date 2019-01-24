from Journal import journal


def print_header():
    print("\n\nWelcome to the Daily Journal")
    print("============================")


def run_event_loop():
    print("\nWhat do?")
    Leave = False
    Entries = Journal.load("yes")

    while (Leave == False):
        choice = input("\n[L] list Entries, [A] Add Entry, [X] to leave: ")

        choice = choice.lower().strip()

        if choice == "l":
            print("\nHere's your shit: ")
            list_entries(Entries)

        elif choice == "a":
            add_entry(Entries)

        elif choice == "x":
            Leave = True
            print("Byeeeeee")

        else:
            print("Bad Boi Try again")
    Journal.save("yes", Entries)
    pass


def main():
    print_header()
    run_event_loop()


def add_entry(data):
    entry = input("\nType your shit: ")
    data.append(entry)


def list_entries(data):
    data = reversed(data)
    for count, i in enumerate(data):
        count += 1
        print("Entry {}: {}".format(count, i))


main()
