'''
Problem:
Recall the definition of Newick format from “Distances in Trees” as a way
of encoding trees. See Figure 1 for an example of Newick format applied to an unrooted
binary tree whose five leaves are labeled (note that the same tree can have multiple Newick representations).

Given: A collection of species names representing n taxa.

Return: A list containing all unrooted binary trees whose leaves are these n taxa.
Trees should be given in Newick format, with one tree on each line;
the order of the trees is unimportant.
'''

def get_data_from_file(filename):
    file = open(filename, "r").read()
    data = file.split()
    return data


def get_tree(data):
    l = [data[0]]
    for i in range(1, len(data)-1):
        l.insert(0, '(')
        l.append(',')
        l.append(data[i])
        l.append(')')
    l.append(data[len(data)-1])
    l.append(';')
    return l


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


def get_trees(data):
    all_trees = []
    for i in range(len(data)):
        new_data = shift(data, i)
        all_trees.append(get_tree(new_data))
    return all_trees

data = get_data_from_file("C:\\Users\\pc\\Downloads\\eubt.txt")
tree = get_tree(data)
all_trees = get_trees(data)
for tree in all_trees:
    for element in tree:
        print(element, end="")
    print()
