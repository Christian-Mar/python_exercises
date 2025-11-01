message = "Everybody is welcome to count the vowels!"
vowels = "aeiou" # already lower case
count = 0
for vowel in vowels:
    count += message.lower().count(vowel)
print(count)


