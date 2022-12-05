from collections import Counter


def most_frequent(List):
    occurrence_count = Counter(List)
    return occurrence_count.most_common(5)


word_list = []
with open('some_text', 'r') as t:
    for line in t.readlines():
        strings = line.split()
        for i in strings:
            if not i.isdigit():
                word_list.append(i)
print(most_frequent(word_list))
