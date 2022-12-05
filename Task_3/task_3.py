N = input('Enter the number of numbers N: ')
if not N.isdigit():
    raise ValueError('N must be a number')
file = open('numbers.txt', 'a')
for i in range(int(N)):
    numbers = input('Enter the number N: ')
    file.write(numbers + ' ')
