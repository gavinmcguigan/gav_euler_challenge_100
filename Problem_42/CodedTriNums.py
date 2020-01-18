from globs import *

"""
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these 
    values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
    is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand 
    common English words, how many are triangle words?
"""


def get_word_val(word: str):
    alpha_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    return sum([alpha_code.index(letter) + 1 for letter in word])


def open_file_sort_words():
    with open("p042_words.txt", "r") as f:
        word_list = f.readline().replace('"', '').split(',')

    for word in word_list:
        yield word


def start():
    tri_nums = [int(0.5*i*(i+1)) for i in range(1, 20)]
    g = open_file_sort_words()
    total_tri_words = 0
    for w in g:
        wv = get_word_val(w)
        if wv in tri_nums:
            total_tri_words += 1

    return total_tri_words


if __name__ == '__main__':
    answer = start()
    show_answer(answer)
