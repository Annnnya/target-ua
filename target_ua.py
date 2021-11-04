"""
module name
"""
import random

def generate_grid():
    """
    generates 5 unique random letters
    """
    res = []
    letter_list = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж,' 'з',\
    'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',\
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    while len(res) < 5:
        letter = random.choice(letter_list)
        if letter not in res:
            res.append(letter)
    return res


def get_words(f_name, letters):
    """
    finds right words
    """
    res = []
    letters_set = set(letters)
    with open(f_name, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0] in letters_set:
                line = line.strip().split()
                if len(line[0]) <= 5:
                    if '/n' in line[1] or 'noun' in line[1]:
                        res.append((line[0], "noun"))
                    if line[1].startswith('adj') or line[1].startswith('/adj'):
                        res.append((line[0], "adjective"))
                    if '/v' in line[1]:
                        res.append((line[0], "verb"))
                    if line[1].startswith('adv') or line[1].startswith('/adv'):
                        res.append((line[0], "adverb"))
    return res


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    returns right words and missed words
    >>> check_user_words(['ром', 'абродлд', 'сон'], 'noun',\
['а','б','в','г','р'], [('ром','noun'), ('сон','noun')])
    (['ром'], ['сон'])
    """
    fine_user_words = []
    right_words = []
    missed_words = []
    for word in user_words:
        if word[0] in letters and len(word)<=5:
            fine_user_words.append(word)
    for i in dict_of_words:
        if i[0] in fine_user_words and i[1]==language_part:
            right_words.append(i[0])
        elif i[1]==language_part:
            missed_words.append(i[0])
    return right_words, missed_words
