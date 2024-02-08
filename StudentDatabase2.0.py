def list_names(students):
    print("List of students:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student['name']}")

def get_new_student():
    new_student = {}
    new_student['name'] = input("Enter the student's name: ")
    new_student['hometown'] = input("Enter the student's hometown: ")
    new_student['favorite_food'] = input("Enter the student's favorite food: ")
    return new_student

# Initial list of students
students = [
    { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
    { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
    { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }
]

print("Welcome to the Student Information System!")

while True:
    option = input("Would you like to 'add' a new student, 'view' existing students, or 'quit' the program? ").strip().lower()

    if option == 'quit':
        print("Thank you for using the Student Information System. Goodbye!")
        break

    elif option == 'add':
        new_student = get_new_student()
        students.append(new_student)
        print("Student added successfully!")

    elif option == 'view':
        list_names(students)
        choice = input("Enter the index of the student you want to learn about: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(students):
                student = students[index]
                print(f"Selected student: {student['name']}")
                info_choice = input("Would you like to see their 'hometown' or 'favorite food'? ").strip().lower()
                if info_choice == 'hometown':
                    print(f"{student['name']}'s hometown is: {student['hometown']}")
                elif info_choice == 'favorite food':
                    print(f"{student['name']}'s favorite food is: {student['favorite_food']}")
                else:
                    print("Invalid option! Please enter 'hometown' or 'favorite food'.")
            else:
                print("Invalid index! Please enter a valid index.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    else:
        print("Invalid option! Please enter 'add', 'view', or 'quit'.")
