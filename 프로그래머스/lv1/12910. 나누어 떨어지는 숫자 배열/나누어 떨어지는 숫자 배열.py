def solution(arr, divisor):
    answer = []
    for elem in arr:
        if elem % divisor == 0:
            answer.append(elem)
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return sorted(answer)

'''
[다른 풀이]
def solution(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]
# list 안에서 for 문 + if 문 사용하기
# or 조건으로 앞의 값이 True가 아니면 [-1] 출력
'''
