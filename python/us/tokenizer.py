prefixes = [
    ',', '"', '{', '[', '(', '*', '<', '$',
    '£', '“', '\'', '``', '`', '#', 'US$', 'C$', 'A$',
    'a-', '‘', '....', '...', '…',
]

suffixes = [
    r',',
    r'\"',
    r'\)',
    r'\]',
    r'\}',
    r'\*',
    r'\!',
    r'\?',
    r'\%',
    r'\$',
    r'>',
    r':',
    r';',
    r'\'',
    r'”',
    r'\'\'',
    r'\'s',
    r'\'S',
    r'\’s',
    r'\’S',
    r'\’',
    r'\.\.',
    r'\.\.\.',
    r'\.\.\.\.',
    r'(?<=[a-z0-9)\]"\'%\)])\.',
    r'(?<=[0-9])km',
]

punctuation = ',.'


def tokenizer(string):
    tokens = string.split()
    tokens = flatten([tok.split(punctuation) for tok in tokens])
    return tokens

if __name__ == '__main__':
    print(tokenizer("i am, a sentence."))
