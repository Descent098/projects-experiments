import random
import string
import lorem
import os

if not os.path.exists("output"):
    os.mkdir("output")
ranstring = lambda x: ''.join(random.choices(string.ascii_uppercase, k=x)) # Generates a random 10 character string

ranstring(10)




for _ in range(180):
    contents = f"""---
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
    with open(f"output{os.sep}{ranstring(22)}.md", "w+") as mdfile:
        mdfile.write(contents)