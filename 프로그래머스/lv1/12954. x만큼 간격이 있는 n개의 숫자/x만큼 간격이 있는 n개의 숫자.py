def solution(x, n):
    answer = []
    a = x
    while len(answer) < n:
        answer.append(x)
        x += a
    return answer

'''
[다른 풀이]
def number_generator(x, n):
    # 함수를 완성하세요
    return [i for i in range(x, x*n+1, x)
# range 함수의 2번째 인자를 x*n+1로 설정하면 x가 n만큼 증가된 수까지만 계산할 수 있음 
'''
