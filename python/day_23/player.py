from turtle import Turtle

# Constants for player movement
STARTING_POSITION = (0, -280)  # Starting point of the turtle (player)
MOVE_DISTANCE = 10  # Distance the turtle moves in one step
FINISH_LINE_Y = 280  # Y-coordinate of the finish line (top of the screen)

# Player class handles the movement of the turtle (the player)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the turtle shape to be the player
        self.penup()  # Prevent drawing lines when moving
        self.go_to_start()  # Move the player to the starting position
        self.setheading(90)  # Set the turtle's facing direction upwards

    # Function to move player upward
    def go_up(self):
        self.forward(MOVE_DISTANCE)  # Moves the player forward by a defined distance

    # Function to check if player has reached the top (finish line)
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y  # Check if the player crossed the finish line

    # Function to reset player position after crossing the finish line
    def go_to_start(self):
        self.goto(STARTING_POSITION)  # Reset player to starting position
