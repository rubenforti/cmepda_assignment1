#!/usr/bin/env python
# Copyright (C) 2022 r.forti1@studenti.unipi.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""First assignment for the CMEPDA course, 2022/23. """

# --- Goal
# Write a Python program that prints the relative frequence of each letter
# of the alphabet (without distinguishing between lower and upper case) in the
# book.

# --- Specifications
# - the program should have a --help option summarizing the usage
# - the program should accept the path to the input file from the command line
# - the program should print out the total elapsed time
# - the program should have an option to display a histogram of the frequences
# - [optional] the program should have an option to skip the parts of the text
#   that do not pertain to the book (e.g., preamble and license)
# - [optional] the program should have an option to print out the basic book
#   stats (e.g., number of characters, number of words, number of lines, etc.)


import time
import argparse
import numpy as np
import matplotlib.pyplot as plt


def process(file_path):
    """
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    #print(text)
    print('Done.')
    return text


def count_characters(text_string, dict, letter):
    """
    """
    text_string.lower()
    length = len(text_string)
    dict[letter] = text_str.count(letter, 1, length+1)


if __name__ == '__main__':
    t1 = time.time()
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    args = parser.parse_args()
    text_str = process(args.infile)

    alphabet = {}
    lett = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for l in lett:
        count_characters(text_str, alphabet, l)

    val = list(alphabet.values())
    array = np.array(val)
    s = sum(array)
    array = array*100./s

    plt.bar(lett, array)
    plt.title("Distribuzione delle lettere nel libro")
    plt.ylabel("Occorrenze percentuali")
    plt.grid(linestyle="--", linewidth=0.5)
    plt.savefig("occurrences.png")
    #plt.show()

    t2 = time.time()
    print(f"Durata del programma = {t2-t1} secondi")
