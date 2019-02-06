from Bio import pairwise2
from Bio import SeqIO

seq1 = SeqIO.read("C:\\Users\\pc\\Downloads\\1.fasta", "fasta").seq
seq2 = SeqIO.read("C:\\Users\\pc\\Downloads\\2.fasta", "fasta").seq

print(seq1)
print(seq2)

M = [[3,   0, -1, -4,  -5,  -10, -11],
    [ 0,   3,  0, -1,  -4,  -7,  -10],
    [-1,   0,  3, -2,  -1,  -6,  -7],
    [-4,  -1,  0,  3,   0,  -3,  -6],
    [-7,  -4, -3,  2,   3,   0,  -3],
    [-10, -5, -6, -3,   0,   3,  -2],
    [-11, -10,-5, -6,  -1,  -2,   3]]

K = [[0 for x in range(7)] for y in range(7)]

def generate_matrix(seq1, seq2):
    for x in range(len(seq1)):
        for y in range(len(seq2)):
            if x != 0 or y != 0:
                diff_x_y = abs(x-y)
            else:
                diff_x_y = 0
            if x < y:
                new_seq1 = seq1[diff_x_y:]
                new_seq2 = seq2[:len(seq2)-diff_x_y]
            if x > y:
                new_seq1 = seq1[:len(seq2)-diff_x_y]
                new_seq2 = seq2[diff_x_y:]
            if x == y:
                new_seq1 = seq1
                new_seq2 = seq2
            print("=================", x, y)
            print("new_seq1 ", new_seq1)
            print("new_seq2 ", new_seq2)
            q = pairwise2.align.globalms(new_seq1, new_seq2, 1, -1, -1, 0)
            w = [a[2] for a in q]
            print(q)
            print(w)
            print("max(w) = ", max(w),"diff_x_y*2 = ",diff_x_y*2 )
            K[x][y] = max(w)-diff_x_y*2

generate_matrix(seq1, seq2)

print("KKKKKKKKKKK")
for x in range(len(K)):
    for y in range(len(K[x])):
        print(K[x][y], end=" ")
    print()