def solution(n, m):
    result = []
    # 최대공약수 (1부터 둘 중 작은 수까지 반복문, 최대공약수이므로 점점 작은 수로 반복)
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            result.append(i)
            break
    
    # 최소공배수 (둘 중 큰 수부터 두 수를 곱한 수까지 반복)
    for j in range(max(n, m), (n*m) + 1):
        if j % n == 0 and j % m == 0:
            result.append(j)
            break
    return result
    