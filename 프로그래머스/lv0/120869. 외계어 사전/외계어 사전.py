from itertools import permutations

def solution(spell, dic):
    permute = list(permutations(spell))
    result = [''.join(t) for t in permute]

    for word in dic:
        if word in result:
            return 1
    return 2

# itertools 라이브러리에서 permutations 함수 사용
# spell의 순열을 구한 후 튜플을 join으로 문자열로 변환
# spell로 조합한 문자열 리스트 안에 dic 안의 요소가 있으면 1 아니면 2 반환

'''
[다른 풀이 1]
def solution(spell, dic):
    spell = set(spell)          # spell을 중복 요소가 없는 집합으로 변환 (set())
    for s in dic:               # dic 안의 문자열을 반복해서 가져온 후
        if not spell-set(s):    # sell 집합과 dic 안의 문자열 집합(set(s))의 차집합이 있는지 확인 
            return 1            # 차집합이 없으면 1 (= 집합이 일치)
    return 2                    # 차집합이 있으면 2 (= 집합이 불일치)
[다른 풀이 2]
def solution(spell, dic):               
    for d in dic:                       # dic 안의 요소를 반복해서 가져온 후
        if sorted(d) == sorted(spell):  # d를 오름차순으로 정렬한 값과 spell을 오름차순으로 정렬한 값이 같으면 1
            return 1                    # 다르면 2
    return 2
'''
