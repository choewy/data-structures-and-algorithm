for _ in range(int(input())):
    count, word = input().split(' ')
    count = int(count)
    print(''.join([character*count for character in word]))
