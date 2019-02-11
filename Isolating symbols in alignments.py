'''
Problem:
Say that we have two strings s and t of respective lengths m and n
and an alignment score. Let's define a matrix M corresponding to s and t
by setting Mj,k equal to the maximum score of any alignment that aligns s[j]
with t[k]. So each entry in M can be equal to at most the maximum score of any
alignment of s and t.

Given: Two DNA strings s and t in FASTA format, each having length at most 1000 bp.

Return: The maximum alignment score of a global alignment of s and t, followed by the
sum of all elements of the matrix M corresponding to s and t that was defined above.
Apply the mismatch score introduced in “Finding a Motif with Modifications”.
'''


from Bio import pairwise2
from Bio import SeqIO
import numpy as np
import time

'''First, we need to get sequences from file'''
seq1 = SeqIO.read("C:\\Users\\pc\\Downloads\\1.fasta", "fasta").seq
seq2 = SeqIO.read("C:\\Users\\pc\\Downloads\\2.fasta", "fasta").seq

# print(seq1)
# print(len(seq1))
# print(seq2)
# print(len(seq2))

seq1_len = len(seq1)
seq2_len = len(seq2)

'''Function which returns 1 if symbols are the same and -1 if not'''
def compare_two_symbols(symbol1, symbol2):
    if symbol1 == symbol2:
        return 1.0
    else:
        return -1.0

'''Function which returns maximum align score of alignment(seq1, seq2)'''
def get_max_alignment_score(seq1, seq2):
    if len(seq1) == 0 and len(seq2) != 0:
        return -len(seq2)
    elif len(seq2) == 0 and len(seq1) != 0:
            return -len(seq1)
    else:
        max_score = pairwise2.align.globalms(seq1, seq2, 1, -1, -1, -1, score_only=True)
        if max_score == []:
            return 0
        else:
            return max_score

'''Generate matrix with maximum alignment scores for each j and t'''
def generate_matrix(seq1, seq2, seq1_len, seq2_len):
    M = np.empty([seq1_len, seq2_len])
    for j in range(seq1_len):
        for t in range(seq2_len):
            score_from_left_part = get_max_alignment_score(seq1[:j], seq2[:t])
            middle_score = compare_two_symbols(seq1[j], seq2[t])
            score_from_right_part = get_max_alignment_score(seq1[j+1:], seq2[t+1:])
            M[j][t] = score_from_left_part + middle_score + score_from_right_part
    return M


'''In this function I count maximum alignment score from all scores and sum of all scores'''
def count_max_and_sum(matrix):
    suma = np.sum(matrix)
    maximum = np.amax(matrix)
    return maximum, suma


M = generate_matrix(seq1, seq2, seq1_len, seq2_len)
# print(M)
maximum, suma = count_max_and_sum(M)
print(maximum, suma)

