"""
truthfinder.py - given a statement and a list of truths, determine whether or
                 not the statement is confirmed (always true), plausible
                 (sometimes true), or busted (never true). Thanks Mythbusters.
"""
from .constants import CONFIRMED, BUSTED, PLAUSIBLE
from .utils import invert


def searchForTruthInner(subject, object, truths, contradictions):
    '''
    The truth-finding function that will recursively determine whether or not
    a statement is true.
    '''
    if subject == object:
        return True
    if subject in truths:
        for word in truths[subject]:
            if searchForTruthInner(word, object, truths, contradictions):
                return True
    return False


def searchForTruth(subject, object, truths, contradictions):
    '''
    The truth-finding function that will recursively determine whether or not
    a statement is true.
    '''
    if searchForTruthInner(subject, object, truths, contradictions):
        return CONFIRMED
    elif searchForTruthInner(subject, invert(object), truths, contradictions):
        return BUSTED
    return PLAUSIBLE
