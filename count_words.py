total = 0
count = 0

with open("words.txt", 'r') as f:
        for line in f:
                word = line.strip()
                total = total + 1
                for letter in word: 
                    if letter == "Y" or letter == "y":
                        count = count + 1
        print(total)
        print(f"{count} is the total amount of y's in words.txt")       
 
# The count of Y/y is an inner loop, so it counts all Y/y's

total = 0
count = 0

with open("words.txt", 'r') as f:
        for line in f:
                word = line.strip()
                total = total + 1
                if 'y' in word.lower(): 
                    count = count + 1
        print(total)
        print(count)       
        print(f"{round(count / total * 100)}% or {count} words have at least one 'y' in it")    

# The if-functionality stays in the same for-loop