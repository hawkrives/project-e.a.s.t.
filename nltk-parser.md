# NLTK Parsing of an English Sentence

This document establishes the structures used in the
[Natural Language Toolkit](www.nltk.org) as a series of [classified] functions.
The goal of this document is to establish the BNF for Abstract Syntax Trees of
English sentences. Along the way it may present some techniques for classifying
words as well.

## Categorizing and Tagging Words

This section comes from the [NLTK book](http://www.nltk.org/book_1ed/ch05.html).

### Tokenizing a Sentence

The default implementation of tokenizing a sentence in the nltk is to use the
*punkt* sentence parser and *treebank* part of speech tagger. The nltk developed
a python implementation from a sed script provided by the
[treebank project](http://www.cis.upenn.edu/~treebank/tokenization.html).

This tokenizer splits a sentence based upon various punctuation and
concatenation of words, then returns the separated words.

A tokenizer function will have the following specification:

```
argument: a string, representing the English sentence to be tokenized.
return: an array of tokens to be tagged with part of speech.
```

**Expansion:** Add a sentence parser to this process in order to be able to
parse blocks of text rather than single sentences.

### Tagging Words in a Sentence

After separating the sentence into different parts of speech, we now need to
classify them according to their part of speech. The recommended method (and the
one used in the nltk) is the Averaged Perceptron method.
[This site](https://spacy.io/blog/part-of-speech-pos-tagger-in-python) explains
the Averaged Perceptron method.

This method uses a list of words to establish a set of weights in the training
phase that will be then applied to the words in the testing phase. The training
phase works as follows:

1. Receive a new feature (word, POS tag).
2. Guess the value of the POS tag given the current weights.
3. If the guess is wrong, add +1 to the weight of the correct class and -1 to
the weight of the predicted class.

This method works well, but it lacks convergence (meaning that later examples
affect the model just as much as earlier examples). To overcome this, return the
averaged weight over the number of iterations. Because it locks in its guesses
as each word comes up, it is classified as a greedy algorithm.

We can use this classifier to tag the part of speech of sentences starting with
the first word in the sentence and uses previously tagged words as a context to
predict future words.

A POS tagger will require a training function that takes in a hand-tagged
sentence and return a series of weights for different tokens according to the
part of speech the token is most likely to be within:

```
argument: an array of words that are hand-tagged.
return: a set of weights for each word that can be used to tag part of speech.
```

**Note:** The article recommends the use of the
[Brown Corpus](http://www.hit.uib.no/icame/brown/bcm.html) for training a
POS classifier. The corpus can be downloaded
[here](http://www.nltk.org/nltk_data/).

**TODO:** There may already be a trained set of weights for these tokens in the
English language. If such a set exists, we may be able to port it over and skip
the training session entirely.

The final Tagger will have a similar style:

```
arguments: an array of words and a series of weights for each word
return: an array of tagged words with the most likely part of speech
```

**Expansion:** There are a variety of corpuses of text that are traditionally
used as a training set for these classification algorithms. Explore and compare
the accuracy of the syntax generator within different contexts.

## Construction an Abstract Syntax Tree

This section comes from the [NLTK book](http://www.nltk.org/book_1ed/ch08.html).

### Phase Structure (Context-Free) Grammar

[Classified]

### Dependency Grammar

[Classified]

# Resources on Parsers

Parsers

- [Stanford PCFG parser](http://nlp.stanford.edu/software/lex-parser.shtml)
- [Parsing English in Python](https://spacy.io/blog/parsing-english-in-python)

Grammars for Syntax Trees

- [Lexical Functional Grammar](https://en.wikipedia.org/wiki/Lexical_functional_grammar)
- [Head-Driven Phase Structure Grammar](https://en.wikipedia.org/wiki/Head-driven_phrase_structure_grammar)
- [Tree-Adjoining Grammar](https://en.wikipedia.org/wiki/Tree-adjoining_grammar)
