n, m = map(int, input().split())
baskets = [i for i in range(1, n+1)]
# [1 ~ n]

for i in range(1, m+1):
    a, b = map(int, input().split())
    baskets[a - 1], baskets[b - 1] = baskets[b - 1], baskets[a - 1]

print(*baskets)
