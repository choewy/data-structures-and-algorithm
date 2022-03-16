def printer():
    n, m = map(int, input().split())
    p = [int(x) for x in input().split()]
    t = [x for x in range(n)]
    t[m] = 'M'

    seq = 1
    while True:
        ti = t[0]

        p_max = max(p)
        pi = p[0]

        if pi == p_max:
            if ti == "M":
                break

            p = p[1:len(p)]
            t = t[1:len(t)]
            seq += 1
        else:
            p = p[1:len(p)] + [pi]
            t = t[1:len(t)] + [ti]

    return seq


cnt = int(input())
for _ in range(cnt):
    print(printer())
