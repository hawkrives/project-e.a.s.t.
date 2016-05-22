import sys
import os
import spacy

nlp = spacy.load('en')

with open(sys.argv[1], 'r') as infile:
    sentences = infile.readlines()

def getTokenByDep(doc, deps):
    for token in doc:
        for dep in deps:
            if token.dep_ == dep:
                return token
    return None

absolute_truths = {}
propositions = sentences[:-1]
conclusions = [sentences[-1]]

for sentence in propositions:
    sentence = sentence.strip()
    parse = nlp(sentence)

    subj = getTokenByDep(parse, ['nsubj'])
    obj = getTokenByDep(parse, ['attr', 'acomp'])

    if (subj.lemma_ in absolute_truths):
        absolute_truths[subj.lemma_].append(obj.lemma_)
    else:
        absolute_truths[subj.lemma_] = [obj.lemma_]

if os.getenv('DEBUG'):
    print('DICTIONARY:', absolute_truths)

for sentence in conclusions:
    sentence = sentence.strip()
    parse = nlp(sentence)

    subj = getTokenByDep(parse, ['nsubj'])
    obj = getTokenByDep(parse, ['attr', 'acomp'])

    statement = [subj.lemma_, obj.lemma_]

if os.getenv('DEBUG'):
    print('STATEMENT:', statement)

def searchForTruths(statement, truths):
    if statement[0] == statement[1]:
        return True
    if statement[0] in truths:
        for word in truths[statement[0]]:
            if searchForTruths([word, statement[1]], truths):
                return True
    return False

print(searchForTruths(statement, absolute_truths))
