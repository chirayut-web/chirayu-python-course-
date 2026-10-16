grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for score in scores:
    if score >= 80:
        grade_counts["A"] += 1
    elif score >= 70:
        grade_counts["B"] += 1
    elif score >= 60:
        grade_counts["C"] += 1
    elif score >= 50:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

print(f"\n=== การแจกแจงเกรด ===")
for grade, count in grade_counts.items():
    percentage = (count / num_students) * 100
    print(f"เกรด {grade}: {count}")