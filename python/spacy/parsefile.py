import sys
import spacy
nlp = spacy.load('en')

with open(sys.argv[1], 'r') as infile:
    sentences = infile.readlines()

for sentence in sentences:
    sentence = sentence.strip()
    parse = nlp(sentence)
    print(parse.text)
    for token in parse:
        print (token.pos_, token.tag_, token.lemma_,
               '<-'+token.dep_+'-', token.head, token.orth_)
    print('--------------------------------------------------')
