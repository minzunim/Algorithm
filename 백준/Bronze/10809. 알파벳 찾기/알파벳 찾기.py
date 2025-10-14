s = input()
char_map = {}
result = []

# hash map
for idx in range(len(s)):
    if s[idx] not in char_map:
        char_map[s[idx]] = idx

for al in 'abcdefghijklmnopqrstuvwxyz':
    if al in char_map:
        result.append(char_map[al])
    else:
        result.append(-1)

print(' '.join(map(str, result)))