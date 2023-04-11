def solution(my_string):
    answer = 0
    arr = my_string.split()
    answer += int(arr[0]) # 1번째 인자 더함
    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            answer += int(arr[i+1])
        else:
            answer -= int(arr[i+1])            
    return answer

# 연산기호를 기준으로 split
# + 다음은 더하기 - 다음은 빼기
