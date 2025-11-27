students = []

while True:
    try:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                name = input("Enter student name: ").strip()

                student_exists = False
                for student in students:
                    if student['name'].lower() == name.lower():
                        student_exists = True
                        break

                if student_exists:
                    print(f"Student '{name}' already exists!")
                else:
                    new_student = {
                        'name': name,
                        'grades': []
                    }
                    students.append(new_student)
            case 2:
                if not students:
                    print("No students available.")
                    continue

                name = input("Enter student name: ").strip()

                found_student = None
                for student in students:
                    if student['name'].lower() == name.lower():
                        found_student = student
                        break

                if found_student is None:
                    print(f"Student '{name}' not found!")
                    continue

                print(f"Adding grades for {found_student['name']}:")
                while True:
                    grade_input = input(
                        "Enter a grade (or 'done' to finish): ").strip()

                    if grade_input.lower() == 'done':
                        break

                    try:
                        grade = float(grade_input)
                        if 0 <= grade <= 100:
                            found_student['grades'].append(grade)
                        else:
                            print("Error: Grade must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            case 3:
                if not students:
                    print("No students available.")
                    continue

                print("\n--- Student Report ---")

                averages = []
                valid_students = []

                for student in students:
                    try:
                        if not student['grades']:
                            print(
                                f"{student['name']}'s average grade is N/A.")
                            continue

                        average = sum(student['grades']) / \
                            len(student['grades'])
                        averages.append(average)
                        valid_students.append(student)
                        print(
                            f"{student['name']}'s average grade is {average:.1f}.")

                    except ZeroDivisionError:
                        print(f"{student['name']}'s average grade is N/A.")

                if averages:
                    max_avg = max(averages)
                    min_avg = min(averages)
                    overall_avg = sum(averages) / len(averages)

                    print("---")
                    print(f"Max Average: {max_avg:.1f}")
                    print(f"Min Average: {min_avg:.1f}")
                    print(f"Overall Average: {overall_avg:.1f}")
                else:
                    print("---")
                    print("No grades available for statistics.")

            case 4:
                if not students:
                    print("No students available.")
                    continue

                students_with_grades = [s for s in students if s['grades']]

                if not students_with_grades:
                    print("No students with grades available.")
                    continue

                try:
                    top_student = max(students_with_grades,
                                      key=lambda student: sum(student['grades']) / len(student['grades']))

                    top_average = sum(
                        top_student['grades']) / len(top_student['grades'])

                    print(
                        f"The student with the highest average is {top_student['name']} with a grade of {top_average:.1f}.")

                except Exception as e:
                    print(f"Error finding top student: {e}")

            case 5:
                print("Exiting program.")
                break

            case _:
                print("Invalid choice. Please enter a number between 1-5.")

    except ValueError:
        print("Error: Please enter a valid number (1-5).")
