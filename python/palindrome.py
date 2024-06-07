import re

def palindrome(word):
    clean_word = cleaning_word(word)
    
    word_list = list(clean_word)
    word_list.reverse()
    reversed_word = ''.join(word_list)

    if clean_word == reversed_word:
        return True
    else:
        return False


def cleaning_word(string_word):
    if type(string_word) == int:
        string_word= str(string_word)
        return string_word
    else:
        string_word= str(string_word).lower().replace(" ", "")
        regex = re.compile('[^a-zA-Z]')
        alpha_num_only = re.sub(regex, "", string_word)
        return alpha_num_only

