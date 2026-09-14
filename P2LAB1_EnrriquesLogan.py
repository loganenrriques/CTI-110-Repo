# Logan Enrriques
# 9/14/2026
# P2LAB1
# Calculations for a circle

# Import the value for pi
import math

print(math.pi)

# Get radius from user
radius = input("Enter the radius: ")

# Show the data type of the radius
print(type(radius))

# Convert radius to a float
radius = float(radius)

print()
# Show the data type of the radius
print(type(radius))

# Calculate diameter
diameter = 2 * radius

# Display diameter using f-string
print(f"The diameter of the circle is {diameter:.1f}")

print()

#Calculate circumference
circumference = 2 * math.pi * radius

# Display circumference using f-string
print(f"The circumference of the circle is {circumference:.2f}")

#Calculate area
area = math.pi * radius ** 2

#Display area using f-string
print(f"The area of the circle is {area:,.3f}")