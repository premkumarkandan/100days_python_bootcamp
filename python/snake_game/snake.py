from turtle import Turtle
# initial positions of three turtles for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# step distance for snake movement
MOVE_DISTANCE = 20
# angles to turn during command from keyboard
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.snake_score = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        if self.head.xcor() > 275:
            return False
        else:
            for seg in range(len(self.snake_segments)-1, 0, -1):
                new_x = self.snake_segments[seg - 1].xcor()
                new_y = self.snake_segments[seg - 1].ycor()
                self.snake_segments[seg].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)


