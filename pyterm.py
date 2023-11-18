import os
import sys

def main(verb_only=False, noun_only=False, num_phrases=10):
    if verb_only and noun_only:
        print("You selected only verb and only noun output, those conflict.  Turning both off.")
        verb_only = False
        noun_only = False
    # load the relevant files
    if not verb_only:
        pass
    if not noun_only: 
        pass

    print(f"Current path: { __file__}")

    # pick n words at random from the filesets

    # print out a list of 

if __name__ == "__main__":
    main()