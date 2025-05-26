student_scores = [200,189,190,165,173,189,169,146]
total_score = sum(student_scores)

# max_score = max(student_scores)

maxscore = student_scores[0]
for max_score in student_scores:
    if max_score > maxscore:
        maxscore = max_score

print(maxscore)

