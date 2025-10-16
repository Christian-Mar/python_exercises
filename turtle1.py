import turtle

def polygon(size: int, sides: int):
   bob = turtle.Turtle()
   
   for i in range(sides):
      bob.forward(size)
      bob.left(360/sides)

   turtle.mainloop()

def main():
   polygon(150, 5)

main()

while True:
   pass