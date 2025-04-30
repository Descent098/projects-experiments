# ###### linear interpolation
  
# def interpolation(d, x):
#     output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
  
#     return output
  
# # Driver Code
# data=[[2019, 12124],[2021, 5700]]
  
# year_x=2020
  
# # Finding the interpolation
# print("Population on year {} is".format(year_x),
#              interpolation(data, year_x))

#####################Stripping a number of digits from a float###################
# def strip_digits(num:float, length:int) -> float:
#     num = str(num)
#     before_decimal, after_decimal = num.split(".")[0], num.split(".")[1][:length:]
#     return float(f"{before_decimal}.{after_decimal}")

# print(strip_digits(3.14159, 3))


################################ Flatten list ####################################
# #l0 = [1]
# l1 = [1,2,[3,4,5,6,7,8],9,10]
# #l2 = [[[[[[[[[[[10],9],8],7],6],5],4],3],2],1],0]

# def flatten(unflattened_list:list) -> list:
#     if not unflattened_list: # If list is empty
#         return unflattened_list

#     if isinstance(unflattened_list[0], list): # If the first element is a sublist
#         # Return the flattened form of the first element and concat with flattened form of remainder
#         return flatten(unflattened_list[0]) + flatten(unflattened_list[1:])

#     # Since the current first value is already "flattened" (not a list) move on to flatten the rest
#     return unflattened_list[:1] + flatten(unflattened_list[1:])

# #print(flatten(l0))
# print(flatten(l1))
# #print(flatten(l2))


############## REMOVING EXTENSIONS ###################################
# file_name= r"C:\Users\Kieran\Pictures\Edited Photos\2021\June\P1100794.jpg"

# extension = "." + file_name.split(".")[-1]
# content_manager = Content.get_available_extensions()[extension]
# print(content_manager().get_content(file_name)[1])


############## Testing dict sorting ###################################
# model_dict= {'AdaBoostClassifier()': 0.8101063257934118,
#  'DecisionTreeClassifier()': 0.7317264413290904,
#  'GradientBoostingClassifier()': 0.8080247842665061,
#  'KNeighborsClassifier()': 0.7572879934634902,
#  'RandomForestClassifier()': 0.7962904231530059,
#  'SVC()': 0.8025361228175797}

# sorted_dict_descending = dict(sorted(model_dict.items(),key=lambda x:x[1], reverse=True))

# sorted_dict_ascending = dict(sorted(model_dict.items(),key=lambda x:x[1]))

# print(sorted_dict_ascending)
# print(sorted_dict_descending)

##################################### Fractions #####################################
# from fractions import Fraction

# pc1 = ((10/40)*(9/39)*(8/38))*(30/37)

# pc2 = (10/40)*(9/39)*(8/38)*(7/37)

# Fraction(pc1 * pc2) # Full fraction

# Fraction(pc1 * pc2).limit_denominator() # Minified


############### Invoking the whois module without a need to explicitly install it ####################
# import subprocess
# from whois.parser import WhoisEntry

# domain = "kieranwood.ca"
# executable = "whois"
# r = subprocess.Popen([executable, domain], stdout=subprocess.PIPE)
# text = r.stdout.read().decode()

# print(WhoisEntry.load(domain, text))


##################################### # Worley Noise Generator ######################################
# # http://en.wikipedia.org/wiki/Worley_noise
# # FB36 - 20130216
# import math
# import random
# from tqdm import tqdm
# from PIL import Image, ImageDraw
# imgx = 500; imgy = 500 # image size
# image = Image.new("L", (imgx, imgy))
# draw = ImageDraw.Draw(image)
# pixels = image.load()
# n = 300 # of seed points
# m = random.randint(0, (n - 1)//50) # degree (?)
# seedsX = [random.randint(0, imgx - 1) for i in range(n)]
# seedsY = [random.randint(0, imgy - 1) for i in range(n)]

# # find max distance
# maxDist = 0.0
# print("Beggining generation of distances")
# for ky in tqdm(range(imgy)):
#     for kx in range(imgx):
#         # create a sorted list of distances to all seed points
#         dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in range(n)]
#         dists.sort()
#         if dists[m] > maxDist: maxDist = dists[m]

# # paint
# print("Beggining painting of distances")
# for ky in tqdm(range(imgy)):
#     for kx in range(imgx):
#         # create a sorted list of distances to all seed points
#         dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in range(n)]
#         dists.sort()
#         c = int(round(255 * dists[m] / maxDist))
#         pixels[kx, ky] = c//3

# # label = "N = " + str(n) + " M = " + str(m)
# # draw.text((0, 0), label, (0, 255, 0)) # write to top-left using green color
# image.save(f"WorleyNoise N{str(n)}, M{str(m)}.png", "PNG")


############################# Insertion sort ###########################################

# # Create list
# from random import shuffle        # Used to shuffle keys in list
# n = 12                            # 12 items in the list
# A = [key for key in range(n)]     # numbers 0 to n-1, in this case 0 to 11
# shuffle(A)                        # Shuffle all the keys around so they are out of order

# # Sort list with insertion sort
# for j in range(1, len(A)):        # Start from 2ndth item (index 1) to the end of the list
#     key = A[j]                    # set comparison key to index in list
#     i = j - 1                     # set i to point to the previous key in the list

#     # Go through second iteration to find where to put current key (key[j])
#     while i >= 0 and A[i] > key: # Compare previous key to current key
#         A[i + 1] = A[i]          # ...
#         i = i-1                  # For next iteration check another index back 
#     A[i+1] = key                 # Correct spot has been found so put key in there

# print(A)



########################################### Bubble Sort ###########################################
# Create list
# from random import shuffle              # Used to shuffle keys in list
# n = 12                                  # 12 items in the list
# A = [key for key in range(n)]           # numbers 0 to n-1, in this case 0 to 11
# shuffle(A)                              # Shuffle all the keys around so they are out of order

# # print(f"{A=}")
# # print(f"{len(A)=}")
# for i in range(0, len(A) - 1, 1):
#     # print(f"{i=}")
#     for j in range(len(A) -1, i, -1):
#         # print(f"{j=}")
#         if A[j] < A[j-1]:
#             A[j], A[j-1] = A[j-1], A[j] # Swap A[j] with A[j-1]

# print(A)

########################################### Towers of Hanoi ###########################################

# number = 1

# def move(move_from, move_to):
#     """Prints the move taken in solving the hanoi problem.
#     Parameters
#     ----------
#     move_from(str): Initial pilar of discs
#     move_to(str): Pillar to move the discs to
#     """
#     global number
#     print(f"{number}. Move disc from {move_from} to {move_to}!")
#     number += 1

# def hanoi(num_of_discs, move_from, helper, move_to ):
#     """
#     A function to solve the towers of hanoi problem.
    
#     Parameters
#     ----------
#     num_of_discs(int): How many discs are on the initial pillar
#     move_from(str): Initial pilar of discs
#     helper(str): The pillar to move the discs via (whichever is left)
#     move_to(str): Pillar to move the discs to
#     """
#     if num_of_discs == 0: # Base case
#         pass
#     else: # Solve the remaining puzzle
#         hanoi(num_of_discs-1, move_from, move_to, helper)
#         move(move_from, move_to)
#         hanoi(num_of_discs-1, helper, move_from, move_to )

# if __name__ == "__main__":

#     discs = int(input("How many discs are on the tower?: "))
#     hanoi(discs, "1", "2", "3")



########################################### Testing new ezcv content system ###########################################
# # Standard Lib Dependencies
# import os                                                # Used primarily in path validation
# from collections import defaultdict                      # Used to give dicts default args
# from dataclasses import dataclass                        # Used to improve class performance
# from typing import DefaultDict, List, Tuple, Type, Union # Used to provide accurate type hints


# # Third Party Dependencies
# import exifread            # Used to get metadata of image files
# import markdown            # Used to render and read markdown files
# from colored import fg     # Used to highlight output with colors, especially errors/warnings

# @dataclass
# class Content(dict):
#     """Base class for other Content types

#     Notes
#     -----
#     - All subclasses are assumed to have implemented:
#         - __metadata__(); Returns a defaultdict of metadata
#         - __html__(); Returns the HTML to render

#     Methods
#     -------
#     get_available_extensions() -> DefaultDict[str, Type]:
#         Returns a defaultdict of available extensions and corresponding types to render them

#     Raises
#     ------
#     NotImplementedError
#         If any of __metadata__(), or __html__() are not implemented in subclass
#     """


#     def get_available_extensions() -> DefaultDict[str, Type]:
#         """Returns a defaultdict of extensions and corresponding child types to handle them

#         Returns
#         -------
#         DefaultDict[str, Type]:
#             A defaultdict with a str for the extension as a key, and the type as a value
#         """
#         all_extensions:DefaultDict[str, Type] = defaultdict(lambda:False)
#         for current_class in Content.__subclasses__():
#             for extension in current_class.extensions:
#                 all_extensions[extension] = current_class
#         return all_extensions


#     def __metadata__(self):
#         """A function to be replaced with the specific implementation of generating metadata defauldict

#         Raises
#         ------
#         NotImplementedError
#             If the function is not implemented in the subclass
#         """
#         raise NotImplementedError


#     def get_content(self, file_path:str):
#         """Generates the metadata and HTML from a peice of content

#         Parameters
#         ----------
#         file_path : str
#             The path to the md file

#         Raises
#         ------
#         NotImplementedError
#             If the function is not implemented in the subclass
#         """
#         raise NotImplementedError


#     def __html__(self, file_path:str):
#         """A function to be replaced with the specific implementation of generating HTML

#         Parameters
#         ----------
#         file_path: (str)
#             The path for the file

#         Raises
#         ------
#         NotImplementedError
#             If the function is not implemented in the subclass
#         """
#         raise NotImplementedError


# @dataclass
# class Markdown(Content):
#     """Used for parsing markdown content

#     Examples
#     --------
#     ```
#     from ezcv.content import Markdown

#     html, metadata = Markdown().get_content('file_1.md')
#     ```
#     """
#     md:markdown.Markdown = markdown.Markdown(extensions=['meta']) # Setup markdown parser with extensions
#     extensions:List[str] = (".md", ".markdown", ".mdown", ".mkdn", ".mkd", ".mdwn")


#     def __metadata__(self) -> defaultdict:
#         """Gets the metadata from the YAML frontmatter of the markdown file

#         Notes
#         -----
#         - This class requires __html__ to be run first, or self.md to be set manually

#         Returns
#         -------
#         defaultdict
#             Returns a defaultdict with the yaml metadata of a peice of content
#         """

#         metadata:defaultdict = defaultdict(lambda:False)
#         for key in self.md.Meta: # Create defaultdict out of metadata
#             if type(self.md.Meta[key]) == list:
#                 metadata[key] = self.md.Meta[key][0]
#             else:
#                 metadata[key] = self.md.Meta[key]
#         return metadata


#     def __html__(self, file_path:str) -> str:
#         with open(f"{file_path}", "r") as mdfile: # Parse markdown file
#             text = mdfile.read()
#         html = self.md.convert(text) # Convert the markdown content text to hmtl
#         return html # Generated in self.__enter__()


#     def get_content(self, file_path: str) -> Tuple[str, defaultdict]:
#         """Gets the html content of a file, and the metadata of the file

#         Parameters
#         ----------
#         file_path : str
#             The path to the file to render

#         Returns
#         -------
#         str, defaultdict
#             Returns the html first as a string and a defaultdict of the metadata

#         Raises
#         ------
#         FileNotFoundError
#             If the provided file path does not exist

#         Examples
#         --------
#         Render a file called file_1.md
#         ```
#         from ezcv.content import Markdown

#         html, metadata = Markdown().get_content('file_1.md')
#         ```
#         """
#         if not os.path.exists(file_path): # If file doesn't exist
#             raise FileNotFoundError(f"{fg(1)} Could not find file: {file_path}{fg(15)}\n")
#         html = self.__html__(file_path)
#         metadata = self.__metadata__()
#         return html, metadata



# @dataclass
# class Image(Content):
#     """
    
#     Notes
#     -----
#     - Exif data is not available on PNG images
#     - Since there are so many conditionals it is recommended to use the existing gallery stylesheet
#     """
#     extensions:List[str] = (".jpg", ".png", ".tiff", ".avix")

#     def __metadata__(self, filename:str) -> defaultdict:
#         """
#         >>> import exifread
#         >>> with open("P1100861.jpg","rb") as f:

#         ...     tags = exifread.process_file(f)    
#         >>> for tag in tags.keys():
#         ...     if not "Thumbnail" in tag:
#         ...             print(f"{tag}, {tags[tag]}")
#         ...
#         Image Make, Panasonic
#         Image Model, DC-G95
#         Image XResolution, 300
#         Image YResolution, 300
#         Image ResolutionUnit, Pixels/Inch
#         Image Software, Adobe Photoshop Camera Raw 13.3 (Windows)
#         Image DateTime, 2021:06:15 11:19:24
#         Image ExifOffset, 206
#         EXIF ExposureTime, 1/125
#         EXIF FNumber, 63/10
#         EXIF ExposureProgram, Manual
#         EXIF ISOSpeedRatings, 800
#         EXIF ExifVersion, 0231
#         EXIF DateTimeOriginal, 2021:06:03 19:14:04
#         EXIF DateTimeDigitized, 2021:06:03 19:14:04
#         EXIF OffsetTime, -06:00
#         EXIF OffsetTimeOriginal, -07:00
#         EXIF OffsetTimeDigitized, -07:00
#         EXIF ShutterSpeedValue, 870723/125000
#         EXIF ApertureValue, 331919/62500
#         EXIF ExposureBiasValue, 0
#         EXIF MaxApertureValue, 85/16
#         EXIF MeteringMode, Pattern
#         EXIF LightSource, Unknown
#         EXIF Flash, Flash did not fire, compulsory flash mode
#         EXIF FocalLength, 400
#         EXIF SubSecTimeOriginal, 045
#         EXIF SubSecTimeDigitized, 045
#         EXIF ColorSpace, sRGB
#         EXIF FocalPlaneXResolution, 49061125/16384
#         EXIF FocalPlaneYResolution, 49061125/16384
#         EXIF FocalPlaneResolutionUnit, 3
#         EXIF SensingMethod, One-chip color area
#         EXIF FileSource, Digital Camera
#         EXIF SceneType, Directly Photographed
#         EXIF CustomRendered, Normal
#         EXIF ExposureMode, Manual Exposure
#         EXIF WhiteBalance, Auto
#         EXIF DigitalZoomRatio, 0
#         EXIF FocalLengthIn35mmFilm, 800
#         EXIF SceneCaptureType, Standard
#         EXIF GainControl, High gain up
#         EXIF Contrast, Normal
#         EXIF Saturation, Normal
#         EXIF Sharpness, Normal
#         EXIF BodySerialNumber, WE9GA002181
#         EXIF LensModel, LEICA DG 100-400/F4.0-6.3
#         EXIF LensSerialNumber, 21AX818G030G
#         """


#         if filename.lower().endswith("jpg") or filename.lower().endswith("tiff"):
#             with open(filename ,"rb") as f:
#                 tags = exifread.process_file(f)
#             tags = defaultdict(lambda:False, tags)
#             return tags
        
#         else:
#             return defaultdict(lambda:False)
        



#     def __html__(self, tags:defaultdict) -> str:
#         """[summary]

#         Returns
#         -------
#         [type]
#             [description]
#         """
#         #TODO: Document class names
#         html = ""

#         if tags['EXIF LensModel']:
#             html += f"<p class='lens'>{tags['EXIF LensModel']}</p>\n"
        
#         if tags['EXIF FocalLengthIn35mmFilm']:
#             if tags['EXIF FocalLengthIn35mmFilm'] != tags['EXIF FocalLength']:
#                 html += f"<p class='focal-length'>{tags['EXIF FocalLengthIn35mmFilm']}mm (full frame equivalent)</p>\n"
#             else:
#                 html += f"<p class='focal-length'>{tags['EXIF FocalLengthIn35mmFilm']}mm</p>\n"
#         else:
#             if tags['EXIF FocalLength']:
#                 html += f"<p class='focal-length'>{tags['EXIF FocalLength']}mm</p>\n"

#         if tags['EXIF ISOSpeedRatings']:
#             html += f"<p class='iso'>ISO {tags['EXIF ISOSpeedRatings']}</p>\n"
#         if tags['EXIF ExposureTime']:
#             html += f"<p class='shutter-speed'>{tags['EXIF ExposureTime']} Second(s)</p>\n"
#         if tags['EXIF FNumber']:
#             from fractions import Fraction
#             html += f"<p class='aperture'>f{str(float(Fraction(str(tags['EXIF FNumber']))))}</p>\n"

#         if tags['Image Make'] and tags['Image Model']:
#             html += f"<p class='camera-type'>{tags['Image Make']} {tags['Image Model']}</p>\n"
#         elif tags['Image Make']:
#             html += f"<p class='camera-type'>{tags['Image Make']}</p>\n"
#         elif tags["Image Model"]:
#             html += f"<p class='camera-type'>{tags['Image Model']}</p>\n"
#         else:
#             ...
#         return html

#     def get_content(self, file_path: str):
#         tags = self.__metadata__(file_path)
#         html = self.__html__(tags)
#         return tags, html

# def get_section_content(section_folder: str, examples: bool = False) -> List[List[Union[defaultdict, str]]]:
#     content:List[List[Union[defaultdict, str]]] = []
#     extension_handlers:DefaultDict[str, Type] = Content.get_available_extensions()
#     filenames:List[str] = []

#     for file_name in os.listdir(section_folder):
#         if not examples and file_name.startswith("example"):
#             continue
#         else:
#             filenames.append(os.path.join(section_folder, file_name))

#     for current_file in filenames:
#         extension = "." + current_file.split(".")[-1]
#         if extension_handlers[extension]:
#             extension_handler = extension_handlers[extension]()
#             metadata, html = extension_handler.get_content(current_file)
#             content.append([metadata, html])
    
#     return content


########################### :) https://www.a1k0n.net/2006/09/15/obfuscated-c-donut.html ########################################

#              k;double sin()
#          ,cos();main(){float A=
#        0,B=0,i,j,z[1760];char b[
#      1760];printf("\x1b[2J");for(;;
#   ){memset(b,32,1760);memset(z,0,7040)
#   ;for(j=0;6.28>j;j+=0.07)for(i=0;6.28
#  >i;i+=0.02){float c=sin(i),d=cos(j),e=
#  sin(A),f=sin(j),g=cos(A),h=d+2,D=1/(c*
#  h*e+f*g+5),l=cos      (i),m=cos(B),n=s\
# in(B),t=c*h*g-f*        e;int x=40+30*D*
# (l*h*m-t*n),y=            12+15*D*(l*h*n
# +t*m),o=x+80*y,          N=8*((f*e-c*d*g
#  )*m-c*d*e-f*g-l        *d*n);if(22>y&&
#  y>0&&x>0&&80>x&&D>z[o]){z[o]=D;;;b[o]=
#  ".,-~:;=!*#$@"[N>0?N:0];}}/*#****!!-*/
#   printf("\x1b[H");for(k=0;1761>k;k++)
#    putchar(k%80?b[k]:10);A+=0.04;B+=
#      0.02;}}/*****####*******!!=;:~
#        ~::==!!!**********!!!==::-
#          .,~~;;;========;;;:~-.
#              ..,--------,*/




from itertools import chain, combinations

def powerset(inputs):
    """Returns the powerset of a set of inputs (all possible combinations)

    Parameters
    ----------
    inputs : Tuple[Tuple[int]]
        The list of inputs to return the powerset of

    Returns
    -------
    List[Tuple[Tuple[int]]]
        A list of tuples that represent all possible combinations of the inputs (including empty set)

    Examples
    --------
    ```
    powerset([1,2,3]) --> [(), (1), (2), (3), (1,2), (1,3), (2,3), (1,2,3)]
    ```
    """
    s = list(inputs)

    n = []
    for r in range(len(s)+1):
        # Get combinations for current r
        ## i.e. s=[1,2,3] r=2, then [(1,2), (1,3), (2,3)]
        combination_sets = [y for y in combinations(s, r)]
        # Combine all combination sets into master list
        for combination_set in combination_sets:
            n.append(combination_set)
    return n


def knapsack(inputs, capacity):
    """Takes in a list of inputs, and gives back a tuple 
    containing the highest value combination that is under
    the weight of the capacity, and it's items that comprise it

    Parameters
    ----------
    inputs : Tuple[Tuple[int]]
        The input items

    capacity : int
        The amount of weight the knapsack can carry

    Returns
    -------
    Tuple[int, Tuple[Tuple[int]]]
        A tuple in the form (value, items) with the highest 
        value for items that fit in the weight limit (capacity)
    """
    powerset_of_inputs = powerset(inputs)
    current_highest = {"value":0, "items":[]}

    for current_set in powerset_of_inputs:

        # Check current set weight does not exceed capacity
        total_weight = 0
        value = 0
        for n in current_set:
            total_weight += n[1]
            value += n[0]
        if total_weight > capacity:
            continue

        if value > current_highest["value"]:
            current_highest["value"] = value
            current_highest["items"] = current_set

    return current_highest["value"], current_highest["items"]