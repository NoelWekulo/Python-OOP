class Student:
    def __init__(self, name):
        # Initialize student with name only; marks will be added later
        self.name = name
        self.marks = []

    def input_marks(self):
        # Prompt the user to enter marks for three subjects
        for i in range(1, 4):
            while True:
                try:
                    mark = float(input(f"Enter mark for subject {i}: "))
                    self.marks.append(mark)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def calculate_average(self):
        # Calculate and return the average of the marks
        return sum(self.marks) / len(self.marks)

    def determine_grade(self):
        # Determine the grade based on the calculated average
        average = self.calculate_average()
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

    def display_info(self):
        # Display student's name, average mark, and grade
        average = self.calculate_average()
        grade = self.determine_grade()
        print(f"\nStudent: {self.name}")
        print(f"Average Mark: {average:.2f}")
        print(f"Grade: {grade}")

# Main code to create a Student instance and interact with the user
name = input("Enter the student's name: ")
student = Student(name)
student.input_marks()
student.display_info()
