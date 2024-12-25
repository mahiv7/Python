def calculate_average(grades):
  """Calculates the average of a list of grades."""
  if not grades:
    return 0
  return sum(grades) / len(grades)

def get_letter_grade(average):
  """Determines the letter grade based on the average score."""
  if average >= 90:
    return 'A'
  elif average >= 80:
    return 'B'
  elif average >= 70:
    return 'C'
  elif average >= 60:
    return 'D'
  else:
    return 'F'

def analyze_student(student_name, grades):
  """Analyzes a student's performance."""
  average_score = calculate_average(grades)
  letter_grade = get_letter_grade(average_score)
  print(f"Student: {student_name}")
  print(f"Average Score: {average_score:.2f}")
  print(f"Letter Grade: {letter_grade}")
  print("----------------------")

# Example usage:
student1_grades = [90, 85, 92, 88, 95]
student2_grades = [78, 82, 75, 80, 79]
student3_grades = [60, 55, 62, 58, 65]

analyze_student("Alice", student1_grades)
analyze_student("Bob", student2_grades)
analyze_student("Charlie", student3_grades)
