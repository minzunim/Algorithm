def solution(n):
    answer = ''
    arr = [i for i in range(n)]
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer