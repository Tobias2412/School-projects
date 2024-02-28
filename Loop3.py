import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
skull = turtle.Turtle()
skull.speed(2)  # Set the drawing speed

# Set the color and fill attributes
skull.color("white")
skull.fillcolor("white")
skull.begin_fill()

# Draw the mythosaur skull
skull.penup()
skull.goto(0, -100)
skull.pendown()
skull.circle(100)

# Draw the horns
skull.penup()
skull.goto(-40, 20)
skull.pendown()
skull.goto(-80, 80)

skull.penup()
skull.goto(40, 20)
skull.pendown()
skull.goto(80, 80)

# Complete the fill
skull.end_fill()

# Hide the turtle
skull.hideturtle()

# Close the turtle graphics window on click
screen.exitonclick()