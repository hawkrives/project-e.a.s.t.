"""
sylloparser.py - pulls the subject and object out of a proposition.
"""
import spacy
from sys import stderr
print('Loading collective knowledge…', file=stderr, end=' ')
stderr.flush()
nlp = spacy.load('en')
print('loaded.', file=stderr)

SUBTREE_TYPES = ['amod', 'compound', 'npadvmod', 'punct']


def getTokensByDep(doc, deps):
    '''Returns the words/phrases that match a given list of dependencies'''
    filtered = [t for t in doc if t.dep_ in deps]
    for token in filtered:
        modifier_and_noun = ' '.join([t.lemma_ for t in token.subtree
                                      if t.dep_ in deps or t.dep_ in SUBTREE_TYPES])
        just_noun = token.lemma_
        return [modifier_and_noun, just_noun]
    return [None, None]


def getTokensByPOS(doc, pos):
    '''Returns the words that match a given list of parts of speech'''
    return [t for t in doc if t.pos_ in pos]


def sylloparse(sentence):
    '''Extracts relevant information from a proposition'''

    # Strip the sentence to remove extra whitespace tokens
    sentence = sentence.strip()

    # Run the spaCy parser on the sentence
    parse = nlp(sentence)

    # Confirm that the sentence is actually a proposition. Currently, we only
    # support sentences that include a form of the verb 'be'
    verbs = getTokensByPOS(parse, ['VERB'])
    if not any([v.lemma_ == 'be' for v in verbs]):
        msg = 'Warning: "{}" does not have "be" as a verb. Ignoring sentence.'.format(parse.text)
        print(msg, file=stderr)
        return None, None, None

    # We have a valid proposition, so we need to get the entity for the
    # subject and the entity for the object of the proposition. The subject
    # implies the object.
    subj = getTokensByDep(parse, ['nsubj'])
    obj = getTokensByDep(parse, ['attr', 'acomp'])

    # Check to see if there is a form of not in the sentence. If there is,
    # then we need to perform additional checks to determine the logic of this
    # proposition. Currently, we negate the object of the proposition if we
    # detect the presence of a negation.
    negs = getTokensByDep(parse, ['neg'])
    if all(negs):
        obj = ['!' + o for o in obj]

    determiners = getTokensByDep(parse, ['det'])
    if determiners[0] and determiners[0] != 'all':
        abs_or_partial = 'partial'
    else:
        abs_or_partial = 'absolute'

    # Return the subject, object dependency as an array.
    return abs_or_partial, subj[0], obj
