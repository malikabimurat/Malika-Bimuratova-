import math

# Convert degree to radian
def degree_to_radian(degree):
    return round(degree * (math.pi / 180), 6)

print(degree_to_radian(15))

# Calculate area of a trapezoid
def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

print(trapezoid_area(5, 5, 6))

# Calculate area of a regular polygon
def regular_polygon_area(sides, length):
    return round((sides * (length ** 2)) / (4 * math.tan(math.pi / sides)), 1)

print(regular_polygon_area(4, 25))

# Calculate area of a parallelogram
def parallelogram_area(base, height):
    return base * height

print(parallelogram_area(5, 6))
