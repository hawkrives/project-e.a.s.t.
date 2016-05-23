def flatten(*args):
    # from http://stackoverflow.com/a/2158532/2347774
    for l in args:
        for el in l:
            if (isinstance(el, list) or isinstance(el, tuple) or isinstance(el, set)) \
                    and not isinstance(el, str):
                yield from flatten(el)
            else:
                yield el


def invert(statement):
    if statement.startswith('!'):
        return statement[1:]
    return '!' + statement


def find_index_in_tuples(lst, word):
    for i, tup in enumerate(lst):
        if word in tup:
            return i
    return None
