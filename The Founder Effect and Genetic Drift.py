'''
Given: Two positive integers N and m, followed by an array A containing k
integers between 0 and 2N. A[j] represents the number of recessive alleles
for the j-th factor in a population of N diploid individuals.

Return: An m×k matrix B for which Bi,j represents the common logarithm of the
probability that after i generations, no copies of the recessive allele for the
j-th factor will remain in the population. Apply the Wright-Fisher model.
'''


import math

'''First, we need to extract data from file'''
def get_data_from_file(filename):
    file = open(filename, "r").read()
    rows = file.split("\n")
    N = int(rows[0].split()[0])
    m = int(rows[0].split()[1])
    alleles_nums = [int(num) for num in rows[1].split()]
    return N, m, alleles_nums

'''Counting frequences for Wright-Fisher model'''
def get_freq(alleles_nums):
    sum = 0
    for allele in alleles_nums:
        sum += allele
    freq = [allele/sum for allele in alleles_nums]
    return freq

'''Counting matrix'''
def count_matrix(m, alleles_nums, N):
    k = len(alleles_nums)
    M = [[0 for j in range(m)] for t in range(k)]
    frequences = get_freq(alleles_nums)
    print(frequences)
    for column in range(k):
        p = math.pow(frequences[column],column)
        q = math.pow((1-frequences[column]), (2*N - alleles_nums[column]))
        M[0][column] = (math.factorial(2*N)/((math.factorial(alleles_nums[column]))*(math.factorial(2*N - alleles_nums[column]))))*p*q
    for row in range(1, m):
        new_freq = [x for x in M[0]]
        for column in range(k):
            p = math.pow(new_freq[column],column)
            q = math.pow((1-frequences[column]), (2*N - alleles_nums[column]))
            M[row][column] = (math.factorial(2*N)/((math.factorial(alleles_nums[column]))*(math.factorial(2*N - alleles_nums[column]))))*p*q

    return M

N, m, alleles_nums = get_data_from_file("C:\\Users\\pc\\Downloads\\foun.txt")
# print(N, m, alleles_nums)
M = count_matrix(m, alleles_nums, N)
for row in range(m):
    for column in range(len(alleles_nums)):
        print(M[row][column], end=" ")
    print()