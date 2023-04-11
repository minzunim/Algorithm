def solution(sides):
    return min(sides) + sum(sides) - max(sides) - 1

# 입출력 예시
# 가장 긴 변이 11인 경우 될 수 있는 나머지 한 변은 5, 6, 7, 8, 9, 10, 11 로 7개입니다.
# max(sides) - (max(sides) - min(sides) + 1) + 1 => min(sides) - 1
# 나머지 한 변이 가장 긴 변인 경우 될 수 있는 한 변은 12, 13, 14, 15, 16, 17 로 6개입니다.
# sum(sides) - 1 - (max(sides) + 1) + 1 => sum(sides) - max(sides)
# 두 경우의 수를 합치면 min(sides) + sum(sides) - max(sides) - 1
