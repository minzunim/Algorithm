n = int(input())
m = list(map(int, input().split()))
total = 0

for score in m:
    total += score / max(m)
    
print(total / n * 100)