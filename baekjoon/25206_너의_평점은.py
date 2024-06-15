import sys
input = sys.stdin.readline


def main():
    grade_score = {
        "A+":4.5,
        "A0":4.0,
        "B+":3.5,
        "B0":3.0,
        "C+":2.5,
        "C0":2.0,
        "D+":1.5,
        "D0":1.0,
        "F":0.0
    }
    score_sum = 0
    score_subject = 0
    
    for _ in range(20):
        name,score,grade = input().strip().split()
        if grade == 'P':
            continue
        score = float(score)
        score_sum += score
        score_subject += (score * grade_score[grade])
    print("%.5f" % float(score_subject/score_sum))

if __name__ == "__main__":
    main()