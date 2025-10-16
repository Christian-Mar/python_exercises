def greeting(*, name:str="friend", time:str="afternoon"):
    return (f"Hello {name}! Good {time}")

print(greeting())
print(greeting(name="Christian", time="morning"))

def doe_iets(f):
    print("Ik ga nu iets doen...")
    f()

def hallo():
    print("Hallo!")

doe_iets(hallo)

