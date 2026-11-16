# Project 02: Student Grade Calculator

# Student Information
student_name = input("Enter Student Name: ")

# Subject Marks
english = float(input("Enter English Marks: "))
mathematic = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))
marathi = float(input("Enter Marathi Marks: "))

# Total Marks Calculation
total_marks = (
    english + mathematic + science +
    computer + hindi + marathi
)

# Percentage % Calculation
percentage = (total_marks / 600) * 100

# Average Calculation
average = total_marks / 6

# Pass or Fail
if (
    english >= 35 and mathematic >= 35 and science >= 35
    and computer >= 35 and hindi >= 35 and marathi >= 35
):

    result = "PASS"
else:
    result = "FAIL"

# Grade Calculation

if result == "FAIL":
    grade = "F"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 35:
    grade = "E"
else:
    grade = "F"

# Display Student Report
print("\n=============== STUDENT REPORT =================")

print("Student Name:", student_name)
print("-" * 35)

print("English Marks:", english)
print("Mathematic Marks:", mathematic)
print("Science Marks:", science)
print("Computer Marks:", computer)
print("Hindi Marks:", hindi)
print("Marathi Marks:", marathi)

print("-" * 35)

print("Total Marks:", total_marks, "/600")
print("Percentage Marks:", round(percentage, 2), "%")
print("Average Marks:", round(average, 2))
print("Final Grade:", grade)
print("Result:", result)

print("=" * 35)