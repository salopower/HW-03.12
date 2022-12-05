from random import randrange
file = open("random_numbers.txt", "w")
for i in range(100):
    numbers = randrange(0, 100)
    file.write(str(numbers) + '\n')
