# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Logic Building Formula

# 1 -> User Inputs - score -> int
# 2 ->  O/p -> str -> A, B



score=int(input("Enter the score :").strip())
print(score)

if score>100 or score<0:
    print("Invalid score")
else:
    if score>=90 and score<=100:
        print("Pass, Your grade is : A")
    elif score>=80 and score<=89:
        print("Pass, Your grade is : B")
    elif score>=70 and score<=79:
        print("Pass, Your grade is : C")
    elif score>=60 and score<=69:
        print("Pass, Your grade is : D")
    else:
        print("Failed, Your grade is : F ")