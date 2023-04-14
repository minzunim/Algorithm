def solution(a, b):
    answer = 0
    if a <= b:
        for num in range(a, b+1):
            answer += num
        return answer
    else:     
        for num in range(b, a+1):
            answer += num 
        return answer
'''
[다른 풀이]
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
# a, b의 값을 비교해서 a가 크면 값을 서로 swap
# range 함수로 합계 구함
'''
