import turtle as t

# Set up the turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a turtle object
pikachu = t.Turtle()
pikachu.speed(1)  # Set the drawing speed (1 is slowest, 0 is fastest)

# Draw Pikachu's body
pikachu.penup()
pikachu.goto(0, -100)
pikachu.pendown()
pikachu.color("yellow")
pikachu.begin_fill()
pikachu.circle(100)
pikachu.end_fill()

# Draw Pikachu's ears
pikachu.penup()
pikachu.goto(0, 0)
pikachu.pendown()
pikachu.color("black")
pikachu.begin_fill()
pikachu.goto(-50, 100)
pikachu.goto(-30, 150)
pikachu.goto(0, 130)
pikachu.end_fill()

pikachu.penup()
pikachu.goto(0, 0)
pikachu.pendown()
pikachu.color("black")
pikachu.begin_fill()
pikachu.goto(50, 100)
pikachu.goto(30, 150)
pikachu.goto(0, 130)
pikachu.end_fill()

# Draw Pikachu's eyes (left eye)
pikachu.penup()
pikachu.goto(-20, 20)
pikachu.pendown()
pikachu.color("black")
pikachu.begin_fill()
pikachu.circle(15)
pikachu.end_fill()

# Draw Pikachu's eyes (right eye)
pikachu.penup()
pikachu.goto(20, 20)
pikachu.pendown()
pikachu.color("black")
pikachu.begin_fill()
pikachu.circle(15)
pikachu.end_fill()

# Draw Pikachu's cheeks (left cheek)
pikachu.penup()
pikachu.goto(-40, -10)
pikachu.pendown()
pikachu.color("red")
pikachu.begin_fill()
pikachu.circle(10)
pikachu.end_fill()

# Draw Pikachu's cheeks (right cheek)
pikachu.penup()
pikachu.goto(40, -10)
pikachu.pendown()
pikachu.color("red")
pikachu.begin_fill()
pikachu.circle(10)
pikachu.end_fill()

# Draw Pikachu's mouth
pikachu.penup()
pikachu.goto(0, -20)
pikachu.pendown()
pikachu.setheading(-60)
pikachu.circle(20, 120)

# Hide the turtle
pikachu.hideturtle()


# Close the drawing window on click
screen.exitonclick()
