import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
pen = turtle.Turtle()
pen.speed(2)

# Define colors
colors = ["yellow", "blue", "green", "red", "purple"]

# Draw the smiley face emoji
pen.up()
pen.goto(0, -100)
pen.down()

# Draw face
pen.begin_fill()
pen.color("yellow")
pen.circle(100)
pen.end_fill()

# Draw eyes
pen.up()
pen.goto(-40, 18)
pen.down()
pen.begin_fill()
pen.color("blue")
pen.circle(20)
pen.end_fill()

pen.up()
pen.goto(40, 20)
pen.down()
pen.begin_fill()
pen.color("blue")
pen.circle(20)
pen.end_fill()

# Draw mouth
pen.up()
pen.goto(-40, -28)
pen.down()
pen.color("red")
pen.width(10)
pen.setheading(-60)
pen.circle(60, 130)


# Exit on click
screen.exitonclick()

