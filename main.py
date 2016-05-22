#!/usr/bin/env python3

"""
main.py - the main file that will parse a series of propositions and evaluate
          their truthfulness.
"""
import sys
import syllogizmos as sg


def print_statement(msg):
    print('Statement: "{}"'.format(msg.strip()))


def print_conclusion(msg):
    print('Conclusion: "{}"'.format(msg.strip()))


def philosophize(sentences):
    '''
    The function that invokes the pipeline and runs all of the code to
    evaluate an argument.
    '''

    # Think about the argument.
    # Rationalize it.
    # Become one with it.

    # Build the collective thought and knowledge of our ancestors, as stated
    # in the propositions.
    absolute_truths = {}
    for sentence in sentences[:-1]:
        print_statement(sentence)
        thought = sg.sylloparse(sentence)

        # Make sure that we have a complete thought
        if not thought:
            continue

        # Do not store repeated knowledge. Instead, collect it.
        if (thought[0] in absolute_truths):
            absolute_truths[thought[0]].append(thought[1])
        else:
            absolute_truths[thought[0]] = [thought[1]]

    # Identify the conclusion, the culmination of all ancestral thought.
    print_conclusion(sentences[-1])
    conclusion = sg.sylloparse(sentences[-1])

    # Find truth from the conclusion, and witness the beauty and order of the
    # universe.
    truth = sg.searchForTruth(conclusion, absolute_truths)
    if truth:
        print('Conclusion: Confirmed.')
    else:
        print('Conclusion: Busted.')


if __name__ == '__main__':
    # Load in the argument from a text file
    with open(sys.argv[1], 'r') as infile:
        lines = infile.readlines()
    philosophize(lines)
