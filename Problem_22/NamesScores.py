""""
    Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it
    into alphabetical order. Then working out the alphabetical value for each name, multiply this value by
    its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""

LETTER_VAL = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
              'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def calc_name_score(pos: int, name: str) -> int:
    letter_sum = 0
    for letter in name:
        letter_sum += LETTER_VAL.get(letter.lower())

    return letter_sum * pos


def open_file_sort_names() -> int:
    total_sum = 0
    with open("names.txt", "r") as f:
        all_txt = f.readline()

    names_list = sorted(all_txt.replace('"', '').split(','))

    for n, name in enumerate(names_list):
        total_sum += calc_name_score(n + 1, name)

    return total_sum


if __name__ == '__main__':
    answer = open_file_sort_names()
    print(f'Answer: {answer}')
