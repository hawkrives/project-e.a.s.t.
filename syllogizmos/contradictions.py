"""
contradictions.py - builds a list of mutually contradictory terms from the tenet
                    of established truths.
"""
import collections


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
    terms = flatten(truths.items())
    unique = set(terms)
    print(unique)
