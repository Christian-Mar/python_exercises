# Zoek het woord dat zorgt voor de meeste anagrammen

# Priemgetallen met caching

# Willekeurige lijst van getallen (lengte onbekend), ieder cijfers ligt tussen 0 en 10, 1 keer over alles lopen, zoek of er voor een getal (vanaf het begin) een supplement bestaat om aan vijftien te komen. 

from pathlib import Path

words_list = Path("words.txt").read_text().splitlines()

def find_most_anagrams(words):
    anagram_dict = {}

    for word in words:
        signature = "".join(sorted(word))
    
        if signature not in anagram_dict:
            anagram_dict[signature] = [word]
        else:
            anagram_dict[signature].append(word)

    longest_anagram_list = [] # find list with most words
    
    for group in anagram_dict.values():
        if len(group) > len(longest_anagram_list):
            longest_anagram_list = group
            
    return longest_anagram_list

resultaat = find_most_anagrams(words_list)
print(f"De grootste groep anagrammen bevat {len(resultaat)} woorden:")
print(resultaat)

# Priemgetallen met memoization (caching)
prime_cache = {}

def is_prime(n):
    """Bepaal of n een priemgetal is, met caching via dictionary."""
    if n in prime_cache:
        return prime_cache[n]

    if n < 2:
        prime_cache[n] = False
        return False

    if n == 2:
        prime_cache[n] = True
        return True

    if n % 2 == 0:
        prime_cache[n] = False
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            prime_cache[n] = False
            return False

    prime_cache[n] = True
    return True

def get_primes_up_to(limit):
    """Geef alle priemgetallen tot en met limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]

# Test
print(f"Priemgetallen tot 50: {get_primes_up_to(50)}")
print(f"Is 97 een priemgetal? {is_prime(97)}")
print(f"Is 100 een priemgetal? {is_prime(100)}")

# Zoek paren die samen 15 maken (in één keer door de lijst)

def find_pair_sum_fifteen(numbers):
   
    seen = {}

    for num in numbers:
        supplement = 15 - num

        if supplement in seen:
            return (supplement, num)

        seen[num] = True

    return None


random_list = [1, 3, 7, 8]


print(f"List: {random_list}")

result = find_pair_sum_fifteen(random_list)
if result:
    num1, num2 = result
    print(f"Found: {num1} + {num2} = 15")
else:
    print("Found nothing")

