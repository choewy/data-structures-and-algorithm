h, m = map(int, input().split(' '))

t = h*60 + m - 45
t = t + (24 * 60) if t < 0 else t

print(f'{t // 60} {t % 60}')
