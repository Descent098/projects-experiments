# This is some testing code for playing around with automated preview rebuilding on file changes in ezcv https://github.com/Descent098/ezcv

import sys     # Used to read input arguments
import time    # used to create artificial delays
import logging # Used to help log in the logging example

# Watchdog is used to "watch" folders and do things when changes happen (create, update, delete files)
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    # Custom fileSystem handler for watching files on the local system
    def on_any_event(self, event):
        """Overriding the method on watchdog.events.FileSystemEventHandler that is called on any file system event"""
        print(f"File {event.src_path} was {event.event_type}, rebuilding")
        # Have it call preview here
        print("Please refresh <insert path here> to see changes")

if __name__ == "__main__": # Call method on change example
    path = sys.argv[1] if len(sys.argv) > 1 else '.' # The path to watch
    event_handler = MyHandler() # Instantiate an event handler
    observer = Observer()       # Instantiate an observer to "watch" the event hendler
    observer.schedule(event_handler, path, recursive=True) # Schedule the observer to watch the event handler on the provided path (and include recursive changes to sub-paths)
    observer.start() # Start the watching
    # Wait one second between polling the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() # Keep program running until termination


# # Log changes example
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S') # Setup a basic logger
#     path = sys.argv[1] if len(sys.argv) > 1 else '.' # get path to watch
#     event_handler = LoggingEventHandler()            # Create a handler that uses the logger to log
#     observer = Observer()       # Instantiate an observer to "watch" the event hendler
#     observer.schedule(event_handler, path, recursive=True) # Schedule the observer to watch the event handler on the provided path (and include recursive changes to sub-paths)
#     observer.start() # Start the watching
#     # Wait one second between polling the observer
#     try:
#         while True:
#             time.sleep(1)
#     finally:
#         observer.stop()
#         observer.join()
