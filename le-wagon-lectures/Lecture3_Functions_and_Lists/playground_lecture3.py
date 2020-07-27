# TODO: it's a playground, let's write some code (no unit tests to run here)

# Circle Exercise
import math


# Use functions to build the same features as in playground_lecture1
def circle_math(radius):

    # Calculating the perimeter and assigning it to a variable
    perimeter = (round((2 * radius * math.pi), 1))
    # Calculating the area and assigning it to a variable
    area = (round((radius ** 2 * math.pi), 1))

    # Returning the result
    return [perimeter, area]


values = circle_math(5)
print(f"Radius=5 => Perimeter={values[0]}, Area={values[1]}")

values = circle_math(6)
print(f"Radius=6 => Perimeter={values[0]}, Area={values[1]}")
