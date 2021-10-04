# My running document of answering stack overflow questions: https://stackoverflow.com/users/11602400/kieran-wood


######## Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers. #################

# def summer_69(arr:list)->int:
#     result = 0                       # Final sum of numbers not 6,7, 8, or 9
#     if not 6 in arr: # If no six in array
#         return sum(arr)

#     encountered_six = False # A flag set when a six is first encountered
#     for number in arr: # Iterate the input list
#         if not encountered_six and number != 6: # Haven't hit a six yet, and current number isn't six
#             result += number

#         elif number == 6: # Set flag to ignore numbers until a 9 is reached
#             encountered_six =True
        
#         elif encountered_six and number == 9:
#             encountered_six = False # Reset the flag to False and keep summing values
        
#         else: # Encountered a six and not yet hit a nine, ignore the number
#             continue

#     return result

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))


######################## I wish to duplicate the first number within the list by the value of the second number in the list. The results should be: ########################
######################## multiples(1,10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]                                                                          ######################## 
######################## multiples(1,2) == [1, 1]                                                                                                   ######################## 
######################## multiples(10,4) == [10, 10, 10, 10]                                                                                        ########################

# def multiples(number:int, amount:int)-> list:
#     """Takes in a number, and an amount, and returns a list of values of number of length amount

#     Parameters
#     ----------
#     number : int
#         The value to be replicated `amount` times in the result

#     amount : int
#         The amount of `number`s that should be in the list

#     Returns
#     -------
#     list
#         A list of integers of value `number` for `amount` times

#     Examples
#     --------
#     ## Create a list of ten one's
#     ```
#     print(multiples(1,10)) # Prints: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     ```
#     """
    
#     # Setup a string with each number followed by a comma to be split by later
#     temp = f"{number}," * amount 

#     # Return the list split by commas, with each value typecasted to an int and the last empty string removed
#     return [int(number) for number in temp.split(",")[:-1]]

# print(multiples(1,10))



########################   Merge two lists ########################   

# A = [0,2,2,3,4,5]

# B = [1,1,4,4]

# result = []
# for item1, item2 in zip(A,B):
#     result.append([item1, item2])


# Output = [[0,1],[2,1],[2,4],[3,4]]

# print(result)
# print(Output == result)

########################   Count number of words that start with a letter in a file ########################   
# import string

# filename = "test.txt" # Replace with filename

# def count_words_starting_with_letters(filename:str) -> dict:
#     """Take in a filename and return a dict with the count of how many words began with each letter

#     Parameters
#     ----------
#     filename : str
#         The filename for the file to count the starting letters

#     Returns
#     -------
#     dict
#         Returns a dict with the key being each letter, and value being how many words start with that letter
#     """

#     # Setting up a dictionary of all ascii_lowercase letters to be incremented on each one found
#     amounts = {letter:0 for letter in string.ascii_lowercase }
#     with open(filename,'r') as file:
#         # reading each line    
#         for line in file:
#             # reading each word        
#             for word in line.split():
#                 amounts[word[0].lower()] += 1
#     return amounts

################################################ Return the number of significant digits in a number ################################################

from numbers import Number
from fractions import Fraction

def significant_digits(n:Number) -> int:
    """[summary]

    Parameters
    ----------
    n : Number
        The value to check for it's significant digits

    Notes
    -----
    - If value has a decimal then the (len(n) - the decimal character) is returned,
        else it returns the raw length of the string representation
    - In repeating decimal cases precision caps out at 34 significant digits

    Returns
    -------
    int
        The number of significant digits in the provided value

    Raises
    ------
    ValueError
        [description]

    Examples
    --------
    ```
    print(significant_digits(1)==1)               # Prints: True
    print(significant_digits(123)==3)             # Prints: True
    print(significant_digits(1.46589)==6)         # Prints: True
    print(significant_digits(1.123123)==7)        # Prints: True
    print(significant_digits(Fraction(3/4))==3)   # Prints: True
    print(significant_digits(Fraction(1/3))==34)  # Prints: True
    print(significant_digits(Fraction(13/3))==33) # Prints: True
    ```
    """
    if not isinstance(n, Number):
        raise ValueError(f"Provided value {n} is not an integer or float") # Error out when not int or float    

    n = str(n)
    if "." in n:
        return len(n.replace(".","")) # Floats/decimals need to remove the period, then count the digits for significant digits
    if type(n) == Fraction:
        return len(str(float(n)).replace(".","")) # Floats/decimals need to remove the period, then count the digits for significant digits
    else:
        return len(str(n)) # Integers have the same number of digits as significant digits


print(significant_digits(1)==1)               # Prints: True
print(significant_digits(123)==3)             # Prints: True
print(significant_digits(1.46589)==6)         # Prints: True
print(significant_digits(1.123123)==7)        # Prints: True
print(significant_digits(Fraction(3/4))==3)   # Prints: True
print(significant_digits(Fraction(1/3))==34)  # Prints: True
print(significant_digits(Fraction(13/3))==33) # Prints: True

################################################
