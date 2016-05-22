"""
truthfinder.py - given a statement and a list of truths, determine whether or
                 not the statement is confirmed (always true), plausible
                 (sometimes true), or busted (never true). Thanks Mythbusters.
"""


def searchForTruth(statement, truths):
    '''
    The truth-finding function that will recursively determine whether or not
    a statement is true.
    '''
    if statement[0] == statement[1]:
        return True
    if statement[0] in truths:
        for word in truths[statement[0]]:
            if searchForTruth([word, statement[1]], truths):
                return True
    return False
