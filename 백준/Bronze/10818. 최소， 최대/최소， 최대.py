count = int(input())
arr = list(map(int, input().split()))
result = str(min(arr)) + ' ' + str(max(arr))
print(result)