# Write a Python program that defines a Student class.
# The class should store the student's name and their marks for three subjects.
# It should also have a method to calculate the student's average mark and determine their
# grade based on the average.
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_average(self):
        # Calculate and return the average of the three marks
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def determine_grade(self):
        # Get the average and determine the grade based on it
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
        # Print out the student’s info, average, and grade
        average = self.calculate_average()
        grade = self.determine_grade()
        print(f"My name is {self.name}, my average mark is {average:.2f}, and my grade is {grade}")

# Example usage
student1 = Student('Noel', 70, 90, 80)
student1.display_info()





