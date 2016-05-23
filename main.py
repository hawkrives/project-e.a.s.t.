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
    absolute_truths = {}
    for sentence in sentences[:-1]:
        print_statement(sentence)
        subjects, objects = sg.sylloparse(sentence)

        # Make sure that we have a complete thought
        if not subjects or not objects:
            continue

        # Do not store repeated knowledge. Instead, collect it.
        for subject in subjects:
            for object in objects:
                if (subject in absolute_truths):
                    absolute_truths[subject].add(object)
                else:
                    absolute_truths[subject] = {object}

    # Discover the dualistic nature of the cosmos.
    contradictions = sg.buildContradictions(absolute_truths)

    # Augment knowledge with the previous discoveries
    # print(absolute_truths)
    absolute_truths = sg.augment_with_contradictions(absolute_truths, contradictions)
    # print(absolute_truths)

    # Identify the conclusion, the culmination of all ancestral thought.
    print_conclusion(sentences[-1])
    conclusion_subj, conclusion_obj = sg.sylloparse(sentences[-1])

    # Find truth from the conclusion, and witness the beauty and order of the
    # universe.
    truth = sg.searchForTruth(conclusion_subj[0], conclusion_obj[0],
                              absolute_truths, contradictions)
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
