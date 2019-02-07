"""
Problem: Given a collection of DNA strings representing contigs,
we use the N statistic NXX (where XX ranges from 01 to 99)
to represent the maximum positive integer L such that the total
number of nucleotides of all contigs having length ≥L is at least
XX% of the sum of contig lengths. The most commonly used such
statistic is N50, although N75 is also worth mentioning.

Given: A collection of at most 1000 DNA strings (whose combined
length does not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
"""

def get_data_from_file(filename):
    file = open(filename, "r")
    data = [len(line.replace("\n", "")) for line in file]
    file.close()
    return data


def get_nx_value(data, procents):
    result = 0
    max_sum = sum(data)*procents/100
    data.sort(reverse=True)
    for i in range(len(data)):
        result += data[i]
        if result >= max_sum:
            return data[i]


"""Example how to use the functions is located below."""

data_from_file = get_data_from_file("C:\\Users\\pc\\Downloads\\rosalind_asmq (1).txt")
N50 = get_nx_value(data_from_file, 50)
N75 = get_nx_value(data_from_file, 75)
print(N50, N75)
