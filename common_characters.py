# Write a Python program that finds the common characters that appear in two given strings.

s1 = 'Hello you!'
s2 = 'python'

common_chars = ''
for c1 in s1.lower():
    if c1 in s2.lower():
        if c1 not in common_chars: # adding the common char only once
            common_chars += c1

print(f'Common characters: {common_chars}')