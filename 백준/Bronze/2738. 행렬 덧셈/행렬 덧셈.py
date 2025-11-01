n, m = map(int, input().split())

# [[1,1,1], [2,2,2], [3,3,3]]

a = [ list(map(int, input().split())) for _ in range(n)]
b = [ list(map(int, input().split())) for _ in range(n)]

for _a, _b in zip(a, b):
    row = ""
    for __a, __b in zip(_a, _b):
        row += str(__a + __b) + " "
    print(row)