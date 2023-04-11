def solution(my_str, n):
    answer = []
    if len(my_str) % n == 0: # n의 배수인 경우
        for i in range(len(my_str) // n):
            answer.append(my_str[i*n:(i+1)*n])
    if len(my_str) % n != 0:
        for i in range(len(my_str) // n):
            answer.append(my_str[i*n:(i+1)*n])
        answer.append(my_str[len(my_str) - len(my_str) % n:])
    return answer

# slice 사용
# 경우를 나눠서 생각 - n의 배수인 경우, n의 배수가 아닌 경우
# n = 2 / len(my_str) = 4 / [:2]를 2번 반복
# n = 4 / len(my_str) = 16 / [:4]를 4번 반복

'''
[다른 풀이]
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
# range(시작, 끝, 증가폭)
# 슬라이싱은 인덱스를 초과해도 에러가 발생하지 않음
'''
