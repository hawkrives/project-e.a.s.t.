"""
contradictions.py - builds a list of mutually contradictory terms from the tenet
                    of established truths.
"""
import collections
from .word_lists import prefixes, opposites
from .utils import flatten


def buildContradictions(absolutes, partials):
    '''Creates a list of contradictory words from statements in the dictonary'''
    # print(truths)
    unique_words = set(flatten(absolutes.items(), partials.items()))
    contradictions = {w: [p + w for p in prefixes
                          if p + w in unique_words]
                      for w in unique_words}
    contradictions = {k: [*opposites.get(k, []), *v]
                      for k, v in contradictions.items()}
    contradictions = [(k, *v) for k, v in contradictions.items()]
    contradictions = [t for t in contradictions if len(t) == 2]
    for k1, v1 in absolutes.items():
        for k2, v2 in absolutes.items():
            for v11 in v1:
                for v22 in v2:
                    if v11 == opposites.get(v22, None) or v22 == opposites.get(v11, None):
                        contradictions.append((k1, k2))
    return contradictions
