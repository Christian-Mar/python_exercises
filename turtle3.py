import turtle

# Scherm instellen
t = turtle.Turtle()

def bloem(aantal_blaadjes, lengte, hoek):
    """Teken een bloem met het gegeven aantal blaadjes."""
    for _ in range(aantal_blaadjes):
        t.circle(lengte, 60)      # eerste helft blaadje
        t.left(120)
        t.circle(lengte, 60)      # tweede helft blaadje
        t.left(360 / aantal_blaadjes)


bloem(7, 180, 120)

turtle.done()

while True:
        pass

