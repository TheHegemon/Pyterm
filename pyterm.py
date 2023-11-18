from os.path import join
import os
import random
import sys

def main(num_phrases=50):
    # load the relevant files
    with open(join('data', 'nouns.txt')) as f:
        noun_list = [line.strip() for line in f]
    with open(join('data', 'adjectives.txt')) as f:
        adj_list = [line.strip() for line in f]
    with open(join('data', 'verbs.txt')) as f:
        verb_list = [line.strip() for line in f]
    with open(join('data', 'adverbs.txt')) as f:
        adv_list = [line.strip() for line in f]

    for idx in range(1, num_phrases + 1):
        noun_or_verb = random.choice(['noun', 'verb'])
        if noun_or_verb == 'noun':
            print(f'{idx}: {random.choice(adj_list)} {random.choice(noun_list)}')
        elif noun_or_verb == 'verb':
            print(f'{idx}: {random.choice(adv_list)} {random.choice(verb_list)}')
        else:
            print('Some error occurred and this did not succeed!  Not sure how it broke though.')

if __name__ == "__main__":
    main()