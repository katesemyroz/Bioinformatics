def get_data_from_file(filename):
    file = open(filename, "r")
    data = [len(line.replace("\n", "")) for line in file]
    file.close()
    return data


def get_nx_value(data, n):
    result = 0
    max_sum = sum(data)*n/100
    data.sort(reverse=True)
    for i in range(len(data)):
        result += data[i]
        if result >= max_sum:
            return data[i]


data_from_file = get_data_from_file("C:\\Users\\pc\\Downloads\\rosalind_asmq (1).txt")
N50 = get_nx_value(data_from_file, 50)
N75 = get_nx_value(data_from_file, 75)
print(N50, N75)
