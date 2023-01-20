def getGrade(score):
    score = score if(score < 80) else 80
    score = score -42 if score > 49 else 0
    if(score < 1):
        return 0
    grade = 4 * score / 40
    return .5 * round(grade/.5)

print("*************************************************")
print("Please Enter Number of Student: ",end='')
student=int(input())
print("*************************************************")
score = []
for i in range(student):
    print(f"Please Insert Student {i+1} Score: ", end='')
    score.append(int(input()))

print("*************************************************")
print("Student | Score | Grade")
for i in range(student):
    print(i + 1 ,"|",score[i], "|", getGrade(score[i]))

print("*************************************************")
