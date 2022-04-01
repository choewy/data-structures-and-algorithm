input_list = list(input().upper())
set_list = list(set(input_list))
count_list = [input_list.count(character) for character in s]
max_count = max(count_list)

if count_list.count(max_count) > 1:
    print('?')
else:
    print(set_list[count_list.index(max_count)])
