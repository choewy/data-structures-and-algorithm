characters = ["dz=", "lj", "nj", "d-", "c=", "c-", "s=", "z="]
count = 0
words = input()

for character in characters:
    if character in words:
        words = words.replace(character, "/")
        count += words.count("/")

    if '/' in words:
        words = words.replace('/', '?')

if '?' in words:
    words = words.replace('?', '')

print(count + len(words))
