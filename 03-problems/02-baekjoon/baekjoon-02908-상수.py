# print(max(map(int, [''.join(reversed(e)) for e in input().split(' ')])))

numbers = input().split(' ')

for i, number in enumerate(numbers):
    numbers[i] = int(''.join(reversed(number)))

print(max(numbers))
