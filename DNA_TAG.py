#!/usr/bin/env python3
# DNA_TAG.py

# import Library
import random


class DNASeqGenerator:
    """ class for generating Unique TAG DNA sequences."""

    def __init__(self):
        """
        Initialising the generator with nucleotides
        """
        self.nucleotides = 'ACGT'

    def generate_dna_sequence(self, length):
        """
        Generate a single DNA sequence of a given length.
        :param length: lenght of the sequence
        :return: DNA sequence
        """
        return ''.join(random.choice(self.nucleotides) for _ in range(length))

    def generate_unique_dna_sequences(self, num_sequences, length):
        """
        Generate a set of unique DNA sequences.

        :param num_sequences: The number of unique DNA sequences to generate (1000)
        :param length: length of each DNA sequence
        :return: A list of unique DNA sequences , Returns an empty list if the
        num of sequences requested is greater than the maximum possible unique sequences.
        """
        max_possible_sequences = 4 ** length
        if num_sequences > max_possible_sequences:
            return []
        sequences = set()
        while len(sequences) < num_sequences:
            sequences.add(self.generate_dna_sequence(length))
        return list(sequences)

    def find_minimum_length_for_unique_sequences(self, num_sequences):
        """
       Determine the shortest length of TAG sequences needed to generate a specified number of unique TAGs

       :param num_sequences: The number of unique TAG sequences to generate
       :return: minimum length required to generate the specified number of unique sequences
       """
        dna_len = 1
        while True:
            if len(self.generate_unique_dna_sequences(num_sequences, dna_len)) == num_sequences:
                return dna_len
            dna_len += 1


# setting no of TAGS
num_tags = 1000
generator = DNASeqGenerator()

# Finding the minimum length for unique TAG sequences
dna_length = generator.find_minimum_length_for_unique_sequences(num_tags)

# Generating unique TAGs
unique_dna_sequences = generator.generate_unique_dna_sequences(num_tags, dna_length)

# Displaying the results
print("\n the unique TAGS are : \n ", unique_dna_sequences)
print("\n shortest possible length of DNA sequence", dna_length)
