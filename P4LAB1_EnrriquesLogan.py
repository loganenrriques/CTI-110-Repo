# Logan Enrriques
# 10/12/2026
#Drawing shapes using loops

import turtle

# Set up the turtle drawing object
window = turtle.Screen()

mikey = turtle.Turtle()

# Change color and size
mikey.pensize(5)
mikey.pencolor("orange")


# User a for loop to draw the square
for side in range(4):
    mikey.forward(200)
    mikey.right(90)
    
# Use a while loop to draw the triangle
num = 1
while num <= 3:
    mikey.forward(200)
    mikey.left(120)
    num = num + 1

# Keep this at the bottom
window.mainloop()