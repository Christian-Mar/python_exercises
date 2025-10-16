import turtle

# Scherm instellen
t = turtle.Turtle()
#t.speed(0)
#turtle.bgcolor("white")

def bloem(aantal_blaadjes, lengte, hoek):
    """Teken een bloem met het gegeven aantal blaadjes."""
    for _ in range(aantal_blaadjes):
        t.circle(lengte, 60)      # eerste helft blaadje
        t.left(120)
        t.circle(lengte, 60)      # tweede helft blaadje
        t.left(360 / aantal_blaadjes)

# Eerste bloem (6 blaadjes)
t.penup()
t.goto(-200, 0)
t.pendown()
bloem(6, 100, 60)

# Tweede bloem (9 blaadjes)
t.penup()
t.goto(0, 0)
t.pendown()
bloem(9, 80, 60)

# Derde bloem (18 blaadjes)
t.penup()
t.goto(200, 0)
t.pendown()
bloem(18, 60, 60)

turtle.done()

while True:
   pass