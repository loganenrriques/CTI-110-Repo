# Logan Enrrique
# 10/21/2026
# P4HW1
# Use loop to display score average

# Make empty list
grades_list = []

num_of_grades = int(input("How many grades will you enter? "))

# For loop that gets one grade for each iteration
for i in range(1, num_of_grades + 1):
    # Get the grade
    grade = float(input(f"Enter grade #{i}: "))
    
    # While the input is bad, trap the user in the loop
    while grade < 0 or grade > 100:
        print("INVALID GRADE ENTERED!")
        print("Grade should be between 0 and 100")
        # Ask the suer to re-enter the grade
        grade = float(input(f"Enter grade #{i} again: "))
    # While loop breaks - grade is good :]
    # Add the calidated grade to the list
    grades_list.append(grade)
    
print(grades_list)


