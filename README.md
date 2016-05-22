# Syllogizmos
> Project E.A.S.T. [DECLASSIFIED]

Given a text file, we find list of propositions and a conclusion.

From those props, we build a mapping of relations.

We walk that dictionary of relations to build a dictionary of opposites, which are derived via a hardcoded list of prefixes.

We then apply that dictionary of things to the conclusion to come up with our evaluation, which returns "Confirmed", "Plausible", or "Busted", à la Mythbusters.


## User Guide

### Installation

We used Python 3; you will need to have Python 3.3 or newer installed.

You will need to install our dependency, `spaCy`. They have installation instructions on [their website](https://spacy.io/docs).


### Usage

You will need a text file with several sentences. Each sentence should be on its own line in the text file, and should be a prepositional statement.

That is, each line needs to state a fact.

	Women are mortal.
	Anna is a woman.

The file must end with a conclusion:

	Anna is mortal.

Syllogizmos will return "Confirmed", "Plausible", or "Busted", depending on the outcome of evaluating that statement.


### Example

Given the text file `women.txt` in the `rationalizations` folder that contains the following text,

	Women are mortal.
	Anna is a woman.
	Anna is mortal.

When you run `syllogizmos rationalizations/women.txt`, you will see the result:

	Statement: "Women are mortal."
	Statement: "Anna is a woman."
	Conclusion: "Anna is mortal."
	Conclsion: Comfirmed.


## Background Information
