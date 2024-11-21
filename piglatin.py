#!/usr/bin/env python3

import argparse


def main():
    words = (args.input).lower().split(' ')
    for word in words:
        if word[0] in 'aeiou':
            print(f"{word}way")
        else:
            new_word = f"{word[1:]}{word[0]}way"
            print(new_word)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='phrase to translate to pig latin.')
    args = parser.parse_args()
    main()
