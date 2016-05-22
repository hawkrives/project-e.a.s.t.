import sys
import os
import spacy

nlp = spacy.load('en')


def getTokenByDep(doc, deps):
    filtered = [t for t in doc if t.dep_ in deps]
    for token in filtered:
        return ' '.join([t.lemma_ for t in token.subtree
                         if t.dep_ in deps or t.dep_ == 'amod'])
    return None


def getTokenByPOS(doc, pos):
    return [t for t in doc if t.pos_ in pos]


def searchForTruths(statement, truths):
    if statement[0] == statement[1]:
        return True
    if statement[0] in truths:
        for word in truths[statement[0]]:
            if searchForTruths([word, statement[1]], truths):
                return True
    return False


def main():
    with open(sys.argv[1], 'r') as infile:
        sentences = infile.readlines()

    absolute_truths = {}
    propositions = sentences[:-1]
    conclusions = [sentences[-1]]

    for sentence in propositions:
        sentence = sentence.strip()
        parse = nlp(sentence)

        # The root of the parse, which is the verb, should be a form of 'be'.
        # Otherwise, we don't have a proposition.
        verbs = getTokenByPOS(parse, ['VERB'])
        if not any([v.lemma_ == 'be' for v in verbs]):
            print('Warning: not using "be" verb. Ignored Sentence "%s"' % parse.text)
            continue

        subj = getTokenByDep(parse, ['nsubj'])
        obj = getTokenByDep(parse, ['attr', 'acomp'])
        negs = getTokenByDep(parse, ['neg'])

        if (negs):
            obj = '!' + obj

        if (subj in absolute_truths):
            absolute_truths[subj].append(obj)
        else:
            absolute_truths[subj] = [obj]

    if os.getenv('DEBUG'):
        print('DICTIONARY:', absolute_truths)

    for sentence in conclusions:
        sentence = sentence.strip()
        parse = nlp(sentence)

        subj = getTokenByDep(parse, ['nsubj'])
        obj = getTokenByDep(parse, ['attr', 'acomp'])
        negs = getTokenByDep(parse, ['neg'])

        if (negs):
            obj = '!' + obj

        statement = [subj, obj]

    if os.getenv('DEBUG'):
        print('STATEMENT:', statement)

    print(searchForTruths(statement, absolute_truths))


if __name__ == '__main__':
    main()
