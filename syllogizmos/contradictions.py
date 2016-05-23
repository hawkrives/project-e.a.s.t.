"""
contradictions.py - builds a list of mutually contradictory terms from the tenet
                    of established truths.
"""
import collections

def flatten(array):
    '''Flattens a list of any depth'''
    for item in array:
        basestring = (str, bytes)
        if isinstance(item, collections.Iterable) and not isinstance(item, basestring):
            for sub in flatten(item):
                yield sub
        else:
            yield item

def buildContradictions(truths):
    '''Creates a list of contradictory words from statements in the dictonary'''
    terms = flatten([[v, truths[v]] for v in truths])
    unique = list(set(terms))
    print(unique)
