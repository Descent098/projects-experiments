# Calculate number of binary palindromes

# palindromes = []

# def binary_is_palindrome(val:str):
#     if type(val) == int:
#         val = str(bin(val))[2::]
#     if val[::-1] == val and len(val) == 13:
#         return True
#     else:
#         return False

# for number in range(int(0b1111111111111) + 1):
#     if binary_is_palindrome(number):
#         palindromes.append(str(bin(number))[2::])

# from pprint import pprint
# pprint(palindromes)
# print(len(palindromes))

def number_binary_palindromes(bitstring_length:int) -> int:
    """Takes in the length of the bitstringm and returns number
    of palindromes for binary numbers of that length

    Parameters
    ----------
    bitstring_length : int
        The length of the bitstrings

    Returns
    -------
    int
        The number of palindromes of the provided bitstring length
    """
    if bitstring_length < 0:
        raise ValueError("Bistring length cannot be negative")

    bitstring_length = int(bitstring_length) # Explicit cast to integer
    
    if bitstring_length %2 == 0: # Even bitstrings
        return 2^(bitstring_length/2)
    else: # Odd numbers
        return 2^((bitstring_length+1)/2)



