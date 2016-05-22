# This file demonstrates some of the code of spacy, which is a python library
# used in NLP.

# Load the library and the pretrained model.
import spacy
nlp = spacy.load('en')

# Run the full pipeline on the text to get all of the information about the
# sentence. parsed_text is a Doc object (a sequence of tokens) in the spacy
# module.
parsed_text = nlp('She sells seashells down by the seashore.');

# Each token has some useful properties, which we'll examine. Note that each
# property here has two versions, one with an underscore and one without. The
# one with an underscore is the string version, and the one without the
# underscore is an index into the spacy vocabulary. Here are some of the
# properties:
#   lemma - the base of the word with no inflectional suffixes
#   orth  - the original word as it appears in the sentence
#   tag   - a tag that represents the word class and morphological features
#   pos   - a less-detailed version of tag which describes the part of speech
#   head  - in the syntactic tree, this is the parent node
for token in parsed_text:
    print(token.lemma_, token.lemma)
    print(token.orth_, token.orth)
    print(token.tag_, token.tag)
    print(token.pos_, token.pos)
    print('------------------------------')

print('Syntactic Tree:')

for token in parsed_text:
    print(' ', token.orth_, '<-'+token.dep_+'-', token.head)
