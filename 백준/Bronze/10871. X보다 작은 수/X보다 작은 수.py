n, x = map(int, input().split())
numbers = list(map(int, input().split()))
arr = []

for num in numbers:
    if num < x:
        arr.append(str(num))

result = ' '.join(arr)

print(result)