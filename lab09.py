def read_file(filename, max_length):
    with open(filename, 'r') as file:
        for line in file:
            if len(line) > max_length:
                yield line[:max_length]
            else:
                yield line

filename = 'example.txt'
max_length = 100

for line in read_file(filename, max_length):
    print(line)