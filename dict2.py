from pathlib import Path

words = Path("words.txt").read_text().splitlines()

def is_interlocking(word):

    evens = word[::2] # starts at 0, takes 2 steps
    odds = word[1::2] # starts at 1, takes 2 steps
    if evens in words and odds in words:
        return True
    
print(is_interlocking("schooled"))
print(is_interlocking("smoodnak"))