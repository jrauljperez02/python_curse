from turtle import Turtle, up
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    

    def create_snake(self):
        """Add each segment to list SEGMENTS"""
        for position in STARTING_POSITION:
            self.add_segments(position)


    def add_segments(self,position):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto((1000,1000))
        self.create_snake()
        self.head = self.segments[0]



    def move(self):
        pass


    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)


    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)

