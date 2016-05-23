#!/usr/bin/env python3

"""
main.py - the main file that will parse a series of propositions and evaluate
          their truthfulness.
"""
import sys
import argparse
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
    partial_truths = {}
    absolute_truths = {}
    for sentence in sentences[:-1]:
        print_statement(sentence)
        abs_or_partial, subject, objects = sg.sylloparse(sentence)

        # Make sure that we have a complete thought
        if not subject or not all(objects):
            continue

        # Do not store repeated knowledge. Instead, collect it.
        if abs_or_partial == 'absolute':
            truths = absolute_truths
        elif abs_or_partial == 'partial':
            truths = partial_truths

        for object in objects:
            if (subject in truths):
                truths[subject].add(object)
            else:
                truths[subject] = {object}

    # Discover the dualistic nature of the cosmos.
    contradictions = sg.buildContradictions(absolute_truths, partial_truths)

    # Augment knowledge with the previous discoveries
    # print(absolute_truths, partial_truths)
    partial_truths = sg.augment_with_contradictions(partial_truths, contradictions)
    absolute_truths = sg.augment_with_contradictions(absolute_truths, contradictions)
    all_truths = sg.merge_dict(absolute_truths, partial_truths)
    # print(absolute_truths, partial_truths)

    # Identify the conclusion, the culmination of all ancestral thought.
    print_conclusion(sentences[-1])
    abs_or_partial, conclusion_subj, conclusion_obj = sg.sylloparse(sentences[-1])

    # Find truth from the conclusion, and witness the beauty and order of the
    # universe.
    if abs_or_partial == 'partial':
        truths = all_truths
    else:
        truths = absolute_truths

    # print(truths)
    truth = sg.searchForTruth(conclusion_subj, conclusion_obj[0],
                              truths, contradictions)

    if truth == sg.CONFIRMED:
        print('Conclusion: Confirmed.')
    elif truth == sg.PLAUSIBLE:
        print('Conclusion: Plausible.')
    else:
        print('Conclusion: Busted.')


def get_args():
    parser = argparse.ArgumentParser(description='Philosophize about truth.')
    parser.add_argument('file', nargs='+', help='A file to process')
    return parser.parse_args()


def load_file(filename):
    with open(filename, 'r') as infile:
        return infile.readlines()


if __name__ == '__main__':
    # Load in the argument from a text file
    args = get_args()
    for file in args.file:
        print('Syllogizing about ' + file)
        lines = load_file(file)
        philosophize(lines)
        print()
