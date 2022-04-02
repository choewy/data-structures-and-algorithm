word = input()
times = 0

if " " in word:
    times += 2
    word.replace("")

if "OPERATOR" in word:
    times += 11
    word.replace("")

for alphabet in word:
    number = ord(alphabet)
    if number in range(65, 68):
        times += 3
    elif number in range(68, 71):
        times += 4
    elif number in range(71, 74):
        times += 5
    elif number in range(74, 77):
        times += 6
    elif number in range(77, 80):
        times += 7
    elif number in range(80, 84):
        times += 8
    elif number in range(84, 87):
        times += 9
    elif number in range(87, 91):
        times += 10

print(times)
