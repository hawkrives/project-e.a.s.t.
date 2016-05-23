"""
truthfinder.py - given a statement and a list of truths, determine whether or
                 not the statement is confirmed (always true), plausible
                 (sometimes true), or busted (never true). Thanks Mythbusters.
"""
from .constants import CONFIRMED, BUSTED, PLAUSIBLE
from .utils import invert


def searchForTruthInner(statement, truths, contradictions):
    '''
    The truth-finding function that will recursively determine whether or not
    a statement is true.
    '''
    if statement[0] == statement[1]:
        return True
    if statement[0] in truths:
        for word in truths[statement[0]]:
            if searchForTruthInner([word, statement[1]], truths, contradictions):
                return True
    return False


def searchForTruth(statement, truths, contradictions):
    '''
    The truth-finding function that will recursively determine whether or not
    a statement is true.
    '''
    if searchForTruthInner(statement, truths, contradictions):
        return CONFIRMED
    elif searchForTruthInner([statement[0], invert(statement[1])], truths, contradictions):
        return BUSTED
    return PLAUSIBLE
