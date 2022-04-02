# https://choewy.github.io/baekjoon-1193/

X = int(input())

step = 1
term = 2
start = 0
end = 1

while X > end:
    step += 1
    start = end
    end += term
    term += 1

if step % 2:
    print(f"{end+1 - X}/{X - start}")

else:
    print(f"{X - start}/{end+1 - X}")
