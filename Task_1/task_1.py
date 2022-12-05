file = open('test.txt', 'r')
numbers = []
for line in file.readlines():
    strings = line.split()
    for i in strings:
        if i.isdigit():
            numbers.append(int(i))
print(' The numbers is: \n', numbers)
