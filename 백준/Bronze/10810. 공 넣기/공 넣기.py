n, m = map(int, input().split())

# n = 1 ~ n까지 바구니
# m = input 횟수

ball_list = n * [0]

for i in range(1, m+1):
    start, end, value = map(int, input().split())

    for j in range(start, end+1):
        ball_list[j-1] = value

print(*ball_list)