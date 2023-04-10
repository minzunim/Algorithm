def solution(numbers, k):
    answer = 0
    if len(numbers) < 2 * k:
        numbers = numbers * k
    return numbers[2 * (k - 1)]

# k = 2 -> 2 * 1 (2 * (k - 1))
# k = 5 -> 2 * 4 (2 * (k - 1))
# k = 3 -> 2 * 2 (2 * (k - 1))
# k번째 공을 받는 사람의 인덱스는 2 * (k -1)

# 123456123456
# 123123
# 만약 numbers 배열의 길이가 2 * k 보다 작다면 k번 만큼 배열이 반복되어야 함

'''
2 * (k - 1)을 배열의 길이로 나눈 다음 그 나머지를 인덱스로 지정한 풀이도 있음 => 코드 길이가 줄어듦
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
'''
