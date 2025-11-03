matrix = []
max_value = 0   # 전체 최대값 저장
row_pos = 0     # 행 번호
col_pos = 0     # 열 번호

for col in range(9):
    row = list(map(int, input().split())) 
    max_num = max(row)
    index = row.index(max_num)
    max_row = [max_num, col, index]
    matrix.append(max_row)

for [max_num, col, index] in matrix:
    if max_num > max_value:
        max_value, row_pos, col_pos  = max_num, col, index
        
print(max_value)
print(row_pos + 1, col_pos + 1, sep=' ')