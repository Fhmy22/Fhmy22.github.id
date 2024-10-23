import turtle

# Set up the screen
turtle.bgcolor("black")
screen = turtle.Screen()
screen.title("Heart Shape")

# Create a turtle for drawing the heart
heart_turtle = turtle.Turtle()
heart_turtle.shape("triangle")
heart_turtle.speed(1) # Hoderate speed
heart_turtle.color("red")

# Star drawing the heart shape
heart_turtle.begin_fill() # Optimal: Begin filling the heart with color

# Move turtle to starting position
heart_turtle.penup()
heart_turtle.goto(0, -100)
heart_turtle.pendown()

# Draw the left curve of the heart
heart_turtle.left(50)
heart_turtle.forward(133)
heart_turtle.circle(50, 200)

# Draw the top of the heart
heart_turtle.right(140)

# Draw the right curve of the heart
heart_turtle.circle(50,200)
heart_turtle.forward(133)

heart_turtle.end_fill() # Optimal: End filling the heart with color

turtle.done() # Keep the window open until it's clicked