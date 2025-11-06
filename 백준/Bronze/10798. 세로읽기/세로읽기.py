rows = [ input() for _ in range(5) ]
max_len = max([len(row) for row in rows])

letters = ''

for i in range(max_len):
    for j in range(5):
        if i < len(rows[j]):
            letters += rows[j][i]
        
print(letters)
        
    