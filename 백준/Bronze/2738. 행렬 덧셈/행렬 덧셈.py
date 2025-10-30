n, m = map(int, input().split())
A = [ map(int, input().split()) for _ in range(n)]
B = [ map(int, input().split()) for _ in range(n)]

total = [[ x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(A, B)]

for matrix in total:
    print(*matrix)
