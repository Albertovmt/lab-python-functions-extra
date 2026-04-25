def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    new_list = [digit for digit in set(lst)]
    return new_list

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    count = ({'Uppercase count':0},{'Lowercase count':0})
    for char in ' '.join(string).split():
        if char == char.upper():
            count[0]['Uppercase count'] += 1
        elif char == char.lower():
            count[1]['Lowercase count'] += 1 
    return count

import string

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    punctuation = ';:!?,."\''
    for mark in punctuation:
        sentence = sentence.replace(mark,'')
    return sentence

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    punctuation = ';:!?,."\''
    for mark in punctuation:
        sentence = sentence.replace(mark,'')

    return len(' '.join(sentence).split())