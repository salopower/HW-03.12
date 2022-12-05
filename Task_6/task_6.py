sum = 0
with open('numbers.txt', 'r') as n:
    for line in n.readlines():
        strings = line.split()
        for i in strings:
            if i.isdigit():
                sum += int(i)
print('The sum is equal: ', sum)
