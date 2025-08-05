def solution(clothes):
    # headgear: yellow_hat, green_turban -> 2
    # eyewear: blue_sunglasses -> 1
    # 전체 값을 더하고 나머지는 곱하기
    map = {}
    plus = 0
    result = 1
    
    for pair in clothes:
        if pair[1] not in map:
            map[pair[1]] = 1
        else:
            map[pair[1]] += 1
    
    for count in map.values():
        result *= (count + 1)  # 안 입는 경우 포함해서 곱함
        
    return result - 1
    
    