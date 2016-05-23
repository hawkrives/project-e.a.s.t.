"""
contradictions.py - builds a list of mutually contradictory terms from the tenet
                    of established truths.
"""
import collections
from .word_lists import prefixes, opposites
from .utils import flatten


def buildContradictions(truths):
    '''Creates a list of contradictory words from statements in the dictonary'''
    unique_words = set(flatten(truths.items()))
    contradictions = {w: [p + w for p in prefixes
                          if p + w in unique_words]
                      for w in unique_words}
    contradictions = {k: [*opposites.get(k, []), *v]
                      for k, v in contradictions.items()}
    contradictions = [(k, *v) for k, v in contradictions.items()]
    contradictions = [t for t in contradictions if len(t) == 2]
    return contradictions
