

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def determine_letter_grade(average):
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

def add_new_student(gradebook):
    name = input("Enter student name: ")
    if name in gradebook:
        print("Student already exists!")
    else:
        gradebook[name] = []
        print(f"Student {name} added successfully!")

def add_grade_to_student(gradebook):
    name = input("Enter student name: ")
    if name not in gradebook:
        print("Student not found!")
        return
    
    try:
        grade = float(input("Enter grade to add: "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100!")
        else:
            gradebook[name].append(grade)
            print(f"Grade {grade} added to {name}'s record.")
    except ValueError:
        print("Invalid grade! Please enter a number.")

def view_student_grades(gradebook):
    name = input("Enter student name: ")
    if name not in gradebook:
        print("Student not found!")
        return
    
    grades = gradebook[name]
    if not grades:
        print(f"{name} has no grades recorded.")
        return
    
    average = calculate_average(grades)
    letter_grade = determine_letter_grade(average)
    
    print(f"\nStudent: {name}")
    print(f"Grades: {', '.join(map(str, grades))}")
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")

def display_class_statistics(gradebook):
    if not gradebook:
        print("No students in the gradebook!")
        return
    
    # Calculate statistics
    class_averages = []
    student_stats = []
    
    for name, grades in gradebook.items():
        if grades:
            avg = calculate_average(grades)
            class_averages.append(avg)
            student_stats.append((name, avg))
    
    if not class_averages:
        print("No grades recorded for any student!")
        return
    
    class_avg = sum(class_averages) / len(class_averages)
    
    # Find highest and lowest performing students
    student_stats.sort(key=lambda x: x[1], reverse=True)
    highest_student, highest_avg = student_stats[0]
    lowest_student, lowest_avg = student_stats[-1]
    
    print("\nClass Statistics:")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Performing Student: {highest_student} ({highest_avg:.2f})")
    print(f"Lowest Performing Student: {lowest_student} ({lowest_avg:.2f})")

def main():
    gradebook = {}
    
    while True:
        print("\nGradebook Menu:")
        print("1. Add new student")
        print("2. Add grade to existing student")
        print("3. View student average and letter grade")
        print("4. Display class statistics")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_new_student(gradebook)
        elif choice == '2':
            add_grade_to_student(gradebook)
        elif choice == '3':
            view_student_grades(gradebook)
        elif choice == '4':
            display_class_statistics(gradebook)
        elif choice == '5':
            print("Exiting gradebook system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()



