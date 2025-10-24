croatias = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
l = input()

for croatia in croatias:
    l = l.replace(croatia, '_')

print(len(l))