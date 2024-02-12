import random


def generate_dna_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))


def generate_unique_dna_sequences(num_sequences, length):
    max_possible_sequences = 4 ** length
    if num_sequences > max_possible_sequences:
        return []
    sequences = set()
    while len(sequences) < num_sequences:
        sequences.add(generate_dna_sequence(length))
    return list(sequences)


# Parameters
num_tags = 1000

# Generating  unique TAGS sequences
tags = []
for dna_length in range(1, num_tags):
    unique_dna_sequences = generate_unique_dna_sequences(num_tags, dna_length)
    if len(unique_dna_sequences) == num_tags:
        break

print(unique_dna_sequences)
print(dna_length)
