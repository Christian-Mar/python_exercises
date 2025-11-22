total = 0
count = 0

with open("words.txt", 'r') as f:
        for line in f:
                word = line.strip()
                total = total + 1
                for letter in word: 
                    if letter == "E" or letter == "e":
                        count = count + 1
        print(total)
        print(count)       
        print(f"{round(count / total * 100)}% has an 'e' in it")    