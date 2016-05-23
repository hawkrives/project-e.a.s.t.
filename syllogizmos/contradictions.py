"""
contradictions.py - builds a list of mutually contradictory terms from the tenet
                    of established truths.
"""
import collections
from .word_lists import prefixes


def flatten(*args):
    # from http://stackoverflow.com/a/2158532/2347774
    for l in args:
        for el in l:
            if (isinstance(el, list) or isinstance(el, tuple)) and not isinstance(el, str):
                yield from flatten(el)
            else:
                yield el


def buildContradictions(truths):
    '''Creates a list of contradictory words from statements in the dictonary'''
    unique_words = set(flatten(truths.items()))
    opposites = {w: [p + w for p in prefixes
                     if p + w in unique_words]
                 for w in unique_words}
    opposites = {k: v for k, v in opposites.items() if v}
    return opposites
