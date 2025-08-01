def solution(sizes):
    # 2차원 배열을 순회하면서 배열의 0번째 요소와 1번째 요소 중 더 큰쪽을 확인하고 큰 걸 첫번째에, 작은걸 두번째에,
    # 두 배열에서 최대값을 구함 (max)
    max_array = []
    min_array = []
    
    for size in sizes:
        max_array.append(max(size))
        min_array.append(min(size))
    return max(max_array) * max(min_array)