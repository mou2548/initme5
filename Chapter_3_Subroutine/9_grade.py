def calculate_percentage(score, total):
    return score/total*100

def grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 75:
        return 'B+'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 65:
        return 'C+'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 55:
        return 'D+'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'
    
score = float(input("My Score : "))
total = float(input("Total Score : "))
percentage = calculate_percentage(score, total)
print(f"My percentage is {percentage:.2f}% and got {grade(percentage)}")