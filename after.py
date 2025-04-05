import math

def area_of_circle(radius):
    return math.pi * radius ** 2

# Example usage:
radius =int(input("enter the number : "))
area = area_of_circle(radius)
print(f"The area of the circle and the perimeter is  {area:.2f}and perimeter is")
