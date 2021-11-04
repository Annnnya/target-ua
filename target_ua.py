from random import sample

def generate_grid():
    """
    generates 5 unique random letters
    """
    letter_list = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж,' 'з', 'и', 'і', 'ї', 'й', 'к',
    'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    return sample(letter_list, 5)


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
                    if 'adj' in line[1]:
                        res.append((line[0], "adjective"))
                    if '/v' in line[1]:
                        res.append((line[0], "verb"))
                    if 'adv' in line[1]:
                        res.append((line[0], "adverb"))
    return res


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    returns right words and missed words
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


         

print(check_user_words(['юрма', 'ютуб', 'юний'], 'noun', ['й', 'ю', 'є', 'ф', 'ь'], get_words('C:/Users/asus/progrexp/lab_6/base.lst', ['й', 'ю', 'є', 'ф', 'ь'])))