word = input().upper()
count_dict = {}

for char in word:
    count_dict[char] = count_dict.get(char, 0) + 1

max_value = max(count_dict.values())
max_keys = [ char for char, count in count_dict.items() if count == max_value ]

if len(max_keys) > 1:
    print('?')
else:
    print(*max_keys)
        
