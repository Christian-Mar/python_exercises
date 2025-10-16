import turtle

def draw_parallelogram(straight_length: float, slanted_length: float, angle: float):
    
    bob = turtle.Turtle()
    bob.speed(1)
    # First straight side
    bob.forward(straight_length)
    bob.left(180 - angle)
    # First slanted side
    bob.forward(slanted_length)
    bob.left(angle)
    # Second straight side
    bob.forward(straight_length)
    bob.left(180 - angle)
    # Second slanted side
    bob.forward(slanted_length)
    bob.left(angle)
    turtle.done()

draw_parallelogram(200, 100, 60)

while True:
   pass
