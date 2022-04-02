n = input()
n = v = f"0{n}" if int(n) < 10 else n

cycle = 0

while True:
    cycle += 1
    v = v[-1] + str(sum(list(map(int, v))))[-1]

    if n == v:
        break

print(cycle)
