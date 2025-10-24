croatias = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
letters = input()
count = 0

for croatia in croatias:
    if croatia in letters:
        letters = letters.replace(croatia, '_')

print(len(letters))