file = open('random_text.txt', 'r')
word = []
for line in file.readlines():
    strings = line.split()
    for i in strings:
        if i.isdigit():
            continue
        else:
            word.append(i)
print(' The numbers of word is: \n', len(word))
