import random

rnd = random.randint
words = ['пара', 'ра', 'рам', 'пам', 'папам', 'па', 'да', 'парам']
vowel = 'а'

def generate_phrase(words) -> str:
    phrase = []
    for i in range(rnd(1, 2)):
        phrase.append(words[rnd(0, len(words) - 1)])
    return '-'.join(phrase)

def generate_verse(words) -> str:
    verse = []
    for i in range(rnd(2, 3)):
        verse.append(generate_phrase(words))
    return ' '.join(verse)

def result(verse: str) -> str:
    print(f'Стих: {verse}')
    res = []

    for phrase in verse.split(' '):
        res.append(list(filter(lambda x: x == vowel, phrase)))

    for i in range(1, len(res)):
        if len(res[i - 1]) != len(res[i]):
            return 'Пам парам'
    return 'Парам пам-пам'



print(f'Ответ: {result(generate_verse(words))}')






