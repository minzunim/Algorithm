
score_table = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total, score_total = 0, 0

for _ in range(20):
    subject, my_score, my_grade = input().split()
    my_score = float(my_score)
    
    for grade, score in score_table.items():
        if my_grade == grade:
            total += my_score * score
            score_total += my_score

print(total / score_total)
