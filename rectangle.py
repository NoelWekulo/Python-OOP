# Exercise 4: Define a Rectangle Class
# Create a class named Rectangle with:
#
# Attributes:
# length (float)
# width (float)
# Methods:
# area: Return the area of the rectangle (length * width).
# perimeter: Return the perimeter of the rectangle (2 * (length + width)).
# Example Usage:

class Rectangle:
    def __init__(self,length:float,width:float):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2

rect1=Rectangle(26.5,23.0)

print(f"the area of a rectangle is : {rect1.area()}")
print(f"the perimeter of the rectangle is {rect1.perimeter()}:")

# Exercise 5: Define a Movie Class with Multiple Methods
# Create a class named Movie with:
#
# Attributes:
# title (string)
# director (string)
# year (integer)
# rating (float)
# Methods:
# display_info: Print "Movie: title by director, released in year. Rating: rating/10".
# update_rating: Update the rating with a new value if within 0 to 10.
class Movie:
    def __init__(self,title,director,year,rating):
        self.title=title
        self.director=director
        self.year=year
        self.rating=rating
    def display_info(self):
        print(f"Movie:{self.title} by {self.director},released in {self.year}.rating:{self.rating}/10")
    def update_rating(self,new_rating):
        if 0 <= new_rating <= 10:
            self.rating = new_rating
            print(f"Rating updated to {self.rating}/10")
        else:
            print("Error: Rating must be between 0 and 10.")


movie1=Movie("The oval","Tyler Perry",2024,2)
movie1.display_info()               # Output: Movie: Inception by Christopher Nolan, released in 2010. Rating: 8.8/10
movie1.update_rating(9.1)           # Updates the rating
movie1.display_info()

