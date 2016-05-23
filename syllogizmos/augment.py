from copy import deepcopy
from .utils import flatten, invert, find_index_in_tuples


def augment_with_contradictions(truths, contradictions):
    all_contradictory_terms = list(flatten(contradictions))
    retval = deepcopy(truths)
    for key, vals in truths.items():
        for word in vals:
            if word in all_contradictory_terms:
                index = find_index_in_tuples(contradictions, word)
                pair = contradictions[index]
                word_to_invert = pair[0] if pair[0] != word else pair[1]
                retval[key].add(invert(word_to_invert))
    return retval
