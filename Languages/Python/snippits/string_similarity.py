# See https://gist.github.com/Descent098/dae85d0235acce5322bf1277d1372a7e

from difflib import SequenceMatcher

# Faster when used with python-Levenshtein, but causes some issues
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



##################### Single word similarity ######################################
def similar_strings(to_compare:str, to_match:str) -> float:
    """Takes in two strings and returns a float of the percentage they are similar to each other

    Parameters
    ----------
    to_compare : str
        The string you want to compare
    to_match : str
        The string you want to compare against

    Returns
    -------
    float
        The ratio of the similarity between to strings
    """
    # Remove excess whitespace
    to_compare = to_compare.strip()
    to_match = to_match.strip()
    return SequenceMatcher(None, to_compare, to_match).ratio()


print(fuzz.ratio("biiiild", "build"))

##################### Word suggestion ######################################

def suggest_word(input_word:str, word_list:str) -> str:
    """Takes in a string and a list of words and returns the most likely word

    Parameters
    ----------
    input_word : str
        The word you want to check for similarity

    word_list : str
        The list of words to test input_word against for similarity

    Returns
    -------
    str
        The most similar word, can also be empty string if none had more than %10 similarity
    """
    similarities = {}
    for current_word in word_list:
        similarities[current_word] = similar_strings(input_word, current_word)
    similarities = dict(sorted(similarities.items(),key=lambda x:x[1], reverse=True))
    print(similarities)
    if list(similarities.values())[0] <= 0.1: # If the most likely suggestion has less than %10 likelyhood
        return ""

    for word in similarities:
        return word         # Return first word in dictionary

print(suggest_word("biiild", ["build", "init", "preview"]))



print(process.extract("biiild", ["build", "init", "preview"], limit=2))