# Prints numbers from staring_number to ending_number-1 in base 10 and binary (i.e. '54: "110110"')

starting_number:int = 0
ending_number:int = 64

def number_to_base(number:int, base:int) -> str:
    """Take a number (in base 10), and represent it in another base

    Parameters
    ----------
    number : int
        The number to convert to a specific base
    base : int
        The base to convert the number to

    Returns
    -------
    str
        The string representation of the value

    Examples
    --------
    Converting 75 between bases
    ```
    number_to_base(75, 2) # returns '1001011'
    number_to_base(75, 16) # returns '4b'
    ```

    Returning results to integer value
    ```
    number, base = 75, 16
    int(number_to_base(75, 16), 16) # Returns 75
    ```
    """
    if base == 16:
        return hex(number)[2::]
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    if len(digits) == 1:
        return str(digits[0])
    else:
        return "".join(digits[::-1])

for i in range(starting_number, ending_number):
    value = 0
    value = number_to_base(i, 2)
    if len(value) < 6:
        padding = abs(6-len(value)) * "0"
        value = padding + value
    print(f'{i}: "{value}"')


# # Simpler loop for ONLY binary
# for i in range(starting_number, ending_number):
#     print(f"{i}: {bin(i)}")

# # Simpler loop for ONLY hex
# for i in range(starting_number, ending_number):
#     print(f"{i}: {hex(i)}")
