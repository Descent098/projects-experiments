import os
from platform import platform
from ctypes import cdll, c_char_p, Structure, POINTER, c_float

# import library
if platform().lower().startswith("windows"):
    lib = cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.realpath(__file__)), "go", "similarity.dll"))
else:
    lib = cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.realpath(__file__)), "go", "similarity.so")) 

# Define the C-compatible User struct in Python
class CSuggestion(Structure):
    _fields_ = [
        ("word", c_char_p),
        ("likelihood", c_float),
    ]




# Setup functions

lib.free_suggestion.argtypes = [POINTER(CSuggestion)]

lib.check_dictionary_similarity.argtypes = [c_char_p]
lib.check_dictionary_similarity.restype = POINTER(CSuggestion)

lib.check_dictionary_similarity_levenstein.argtypes = [c_char_p]
lib.check_dictionary_similarity_levenstein.restype = POINTER(CSuggestion)

def spellcheck(word:str|bytes) -> tuple[str, float]:
    if type(word) == str:
        word = word.strip().lower().encode()
    pointer = lib.check_dictionary_similarity(word)
    try:
        data = pointer.contents
        temp = data.word.decode(errors="replace")

        # Copy out values before clearing
        result = ""
        for character in temp:
            result += str(character)

        # Copy out 2 digits of accuracy for the float
        _, right = str(data.likelihood).split(".")
        likelihood = float(f"{right[0:2]}.{right[2:]}")
        return result, likelihood
    except Exception as e:
        raise Exception(f"Something went wrong during processing: {e}")
    finally:
        lib.free_suggestion(pointer)
        
    
    

if __name__ == "__main__":
    import time
    t1 = time.time()
    word = "almni"
    suggested_word, likelihood = spellcheck("mve")
    print(f"The suggested word for {word} is {suggested_word} with a likelihood of {likelihood}")
    t2 = time.time()
    print(f"Took {(t2-t1)*1000:.3f} miliseconds")
    
