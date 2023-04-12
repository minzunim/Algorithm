# from itertools import permutations

# def solution(spell, dic):
#     permute = list(permutations(spell))
#     result = [''.join(t) for t in permute]
    
#     for word in dic:
#         if word in result:
#             return 1
#     return 2

def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2