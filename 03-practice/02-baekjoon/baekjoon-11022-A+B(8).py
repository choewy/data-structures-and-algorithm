print('\n'.join([f'Case #{i+1}: {a} + {b} = {a + b}' for i, (a, b) in enumerate(
    [list(map(int, input().split(' '))) for _ in range(int(input()))])]))
