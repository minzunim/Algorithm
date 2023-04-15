def solution(n):
    answer = ''
    arr = [i for i in range(n)]
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

'''
[다른 풀이1]
def solution(n):
    return "수박" * (n // 2) + "수" * (n % 2)
# 2로 나눈 몫만큼 '수박'을 더하고 나머지만큼 '수'를 더하기

[다른 풀이2]
def solution(n):
    return "".join(["수박"[i % 2] for i in range(n)])
# '수박'이라는 단어를 '수' 또는 '박'으로 나눠 추가하는 배열을 만들고 join으로 문자열로 합치기
'''
