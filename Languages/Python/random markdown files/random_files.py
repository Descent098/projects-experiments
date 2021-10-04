"""This file is used to generate a bunch of random markdown files"""
import os     # Used to handle paths
import lorem  # Used to generate lorem ipsum on the fly
import random # Used to make random choices of characters
import string # Used to filter by only ascii uppercase in file names

files_to_produce:int = 180 # Amount of random markdown files to produce

if not os.path.exists("output"): # Create folder called output
    os.mkdir("output")

ranstring = lambda x: ''.join(random.choices(string.ascii_uppercase, k=x)) # Generates a random 10 character string

for _ in range(files_to_produce): # Iterate over the number of files to produce and fill them with content
    # The templated content to put inside each markdown file
    contents:str = f"""---
title: {ranstring(3)}
link: https://github.com/Descent098/ezcv
image: https://raw.githubusercontent.com/Descent098/ezcv/master/.github/logo.png
---

{lorem.paragraph()}

{lorem.paragraph()}

{lorem.paragraph()}

{lorem.paragraph()}

{lorem.paragraph()}

{lorem.paragraph()}
    """

    # Create the current file
    with open(f"output{os.sep}{ranstring(22)}.md", "w+") as mdfile:
        mdfile.write(contents)