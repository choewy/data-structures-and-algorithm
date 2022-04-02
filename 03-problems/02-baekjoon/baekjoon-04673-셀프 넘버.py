numbers = [number for number in range(1, 10001)]
results = [number + sum(map(int, list(str(number))))
           for number in range(1, 10001)]
print('\n'.join(map(str, sorted(list(tuple(set(numbers) - set(results)))))))
