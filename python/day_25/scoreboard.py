from turtle import Turtle

# Constants for the scoreboard
FONT = ("Courier", 24, "normal")

# Scoreboard class manages the level display and game-over messages


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize level to 0
        self.penup()
        self.hideturtle()  # Hide the turtle as we don't need to see it
        self.goto(-240, 240)  # Position the scoreboard at the top left
        self.update_scoreboard()  # Call function to display the initial score

    # Function to update the scoreboard with the current level
    def update_scoreboard(self):
        self.clear()  # Clear previous scoreboard to avoid overlap
        self.write(f"Score: {self.score}", align="left", font=FONT)  # Write current level

    # Function to increase the level and update the scoreboard
    def increase_score(self):
        self.score += 1  # Increase level by 1
        self.update_scoreboard()  # Refresh the scoreboard with the new level

    # Function to display "Game Over" message
    def game_over(self):
        self.goto(0, 0)  # Position at the center of the screen
        self.write("GAME OVER", align="center", font=FONT)  # Display game-over message
