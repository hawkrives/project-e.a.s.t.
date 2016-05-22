"""
sylloparser.py - pulls the subject and object out of a proposition.
"""
import spacy
nlp = spacy.load('en')


# This helper function returns the words/phrases that match a given list of
# dependencies
def getTokensByDep(doc, deps):
    filtered = [t for t in doc if t.dep_ in deps]
    for token in filtered:
        return ' '.join([t.lemma_ for t in token.subtree
                         if t.dep_ in deps or t.dep_ == 'amod'])
    return []

# This helper function returns the words that match a given list of parts of
# speech
def getTokensByPOS(doc, pos):
    return [t for t in doc if t.pos_ in pos]

# The parsing function to extract relevant information from a proposition.
def sylloparse(sentence):

    # Strip the sentence to remove extra whitespace tokens
    sentence = sentence.strip()

    # Run the spaCy parser on the sentence
    parse = nlp(sentence)

    # Confirm that the sentence is actually a proposition. Currently, we only
    # support sentences that include a form of the verb 'be'
    verbs = getTokensByPOS(parse, ['VERB'])
    if not any([v.lemma_ == 'be' for v in verbs]):
        print('Warning: not using "be" verb. Ignored Sentence "%s"' % parse.text)
        return None

    # We have a valid proposition, so we need to get the entity for the subject
    # and the entity for the object of the proposition. The subject implies the
    # object.
    subj = getTokensByDep(parse, ['nsubj'])
    obj = getTokensByDep(parse, ['attr', 'acomp'])

    # Check to see if there is a form of not in the sentence. If there is, then
    # we need to perform additional checks to determine the logic of this
    # proposition. Currently, we negate the object of the proposition if we
    # detect the presence of a negation.
    negs = getTokensByDep(parse, ['neg'])
    if negs:
        obj = '!' + obj

    # Return the subject, object dependency as an array.
    return [subj, obj]