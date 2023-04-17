def find_value(data: dict, letter: str):
    for letters in data.keys():
        if letters.__contains__(letter):
            return data[letters]

latin_dict = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}
cyrillic_dict = {'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}

word_value = 0


for letter in input('Введите слово: ').upper():
    if letter.isalpha():
        if letter.isascii():
            word_value += find_value(latin_dict, letter)
        else:
            word_value += find_value(cyrillic_dict, letter)

print(word_value)