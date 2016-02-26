import pickle
import re
from tabulate import tabulate
from save import merge_dictionaries

word_pattern = re.compile('([\w\']*)')

current_candidates = [
    'Carson', 'Cruz', 'Kasich', 'Rubio', 'Trump', 'Sanders', 'Clinton']


def get_candidate_vocabularies(location='downloads/data/master.pickle'):
    ''' returns candidate_vocabularies in the form {candidate: {word: frequency}}
        derived from candidate_remarks {candidate: [remarks]} dictionary 
        pickled at location
    '''
    candidate_remarks = pickle.load(open(location, 'r'))

    candidate_vocabularies = {}  # {cand: {word: freq}}
    for candidate in [name.upper() for name in current_candidates]:
        print 'processing {1} remarks from {0}...'.format(
            candidate, len(candidate_remarks[candidate]))

        candidate_vocabulary = {}

        for remark in candidate_remarks[candidate]:
            candidate_vocabulary[remark] = candidate_vocabulary.get(
                remark, 0) + 1
            words = re.findall(word_pattern, remark)
            for word in words:
                if word != '':
                    candidate_vocabulary[word.lower()] = [
                        candidate_vocabulary.get(word.lower(), 0) + 1
                        ][0]
        candidate_vocabularies[candidate] = candidate_vocabulary

    return candidate_vocabularies, candidate_remarks


def get_highlights(subject_VD, population_VD, proportion):
    ''' returns the list of words most frequently used by the candidate, 
        but are also used only, or in large percentage (proportion) by
        that candidate
    '''
    uniques = []
    for word, frequency in subject_VD.items():
        if frequency > proportion * population_VD[word]:
            uniques.append((word, frequency))
    items = []
    for word, frequency in sorted(uniques, key=lambda x: x[1])[-30:]:
        items += [str(frequency) + ' ' * (5 - len(str(frequency))) + str(word)]
    return items


def print_all_highlights(proportion=0.99, candidates=current_candidates):
    ''' prints a table of most those words most frequently used which are also
        used only (or primarily, controlled by proprotion) by each candidate
    '''
    candidate_vocabularies = get_candidate_vocabularies()[0]
    population_VD = merge_dictionaries(
        [dict(vocabulary) for vocabulary in candidate_vocabularies.values()],
        0)
    highlights = {}
    for candidate in candidates:
        candidate_VD = dict(candidate_vocabularies[candidate.upper()])
        highlights[candidate] = get_highlights(
            candidate_VD, population_VD, proportion)

    # now we print...
    print tabulate(highlights, headers='keys')


# def markov():
#     candies_vocab, candy_remarks = get_candidate_vocabularies()
#     for candy_vocab in candies_vocab:
#         candy_map = {}
#         for word in candy_vocab:

#     pass


if __name__ == '__main__':
    print_all_highlights(0.5)
    # import doctest
    # doctest.run_docstring_examples(
    #     markov, globals(),
    #     verbose=True, name="Jus' Testin'")
    pass
