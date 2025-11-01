# method 1
with open("words.txt", "r") as file:
    lines = file.readlines()

for word in lines:
    print(word.strip())

# method 2
with open("words.txt", "r") as file:
    while True: 
        line = file.readline()
        print(line.strip())

        if not line: 
            break

