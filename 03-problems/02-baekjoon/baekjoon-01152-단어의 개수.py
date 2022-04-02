words = input().split(' ')

if words[0] == "":
    words.pop(0)

if words[-1] == "":
    words.pop()

print(len(words))
