def is_newer(version1, version2):
    """
    Vergelijkt twee versies zonder imports.
    Ondersteunt: getallen, tekst (alpha/beta), dev/prod en ISO-datums.
    """
    
    # 1. Gewichten toekennen aan specifieke termen.
    # Negatieve getallen zijn 'pre-release' (komen VOOR de definitieve versie).
    # 0 is de standaard/neutrale waarde (bv. het ontbreken van een suffix).
    # Positieve getallen zijn nieuwer dan standaard (bv. patches of prod).
    weights = {
        'dev': -20,    'development': -20,
        'alpha': -10,  'a': -10,
        'beta':  -5,   'b': -5,
        'rc':    -1,
        'final':  0,   'stable': 0,
        'prod':   1,   'production': 1
    }

    def parse(v):
        # Maak string, alles lowercase, en normaliseer scheidingstekens naar punt
        s = str(v).lower().replace('-', '.').replace('_', '.').replace('/', '.')
        
        parsed = []
        for part in s.split('.'):
            if not part:
                continue  # Sla lege stukken over (bv 1..2)
            
            if part.isdigit():
                parsed.append(int(part))
            else:
                # Als het woord in onze weights lijst staat, pak die waarde (int)
                # Zo niet, behoud de tekst (str) voor alfabetische vergelijking
                parsed.append(weights.get(part, part))
        return parsed

    p1 = parse(version1)
    p2 = parse(version2)
    
    # Bepaal de maximale lengte om te itereren
    length = max(len(p1), len(p2))
    
    for i in range(length):
        # Haal de waarde op. Als de lijst stopt, nemen we 0 aan.
        # Dit zorgt ervoor dat '1.0' (1, 0) > '1.0.alpha' (1, 0, -10)
        # Want op index 2 vergelijken we 0 (standaard) met -10 (alpha).
        val1 = p1[i] if i < len(p1) else 0
        val2 = p2[i] if i < len(p2) else 0
        
        # Als de types gelijk zijn (int vs int, of str vs str)
        if isinstance(val1, type(val2)):
            if val1 > val2:
                return True
            if val1 < val2:
                return False

        # Als types ongelijk zijn (bv. getal vs tekst), geef prioriteit aan getal.
        # Dit is een ontwerpkeuze: 1.1 > 1.A
        elif isinstance(val1, int) and isinstance(val2, str):
            return True
        elif isinstance(val1, str) and isinstance(val2, int):
            return False
            
    # Als we hier komen zijn ze exact gelijk
    return False

# --- Test Suite ---

# Basis Asserties
print(f"is_newer(2, 1) = {is_newer(2, 1)}")
assert is_newer(2, 1)

print(f"is_newer('2.1', '1.2') = {is_newer('2.1', '1.2')}")
assert is_newer("2.1", "1.2")

print(f"is_newer('2.1.1', '2.1.0') = {is_newer('2.1.1', '2.1.0')}")
assert is_newer("2.1.1", "2.1.0")

print(f"is_newer('2.1.1', '10.1.1') = {is_newer('2.1.1', '10.1.1')}")
assert not is_newer("2.1.1", "10.1.1")

print(f"is_newer('1.B', '1.A') = {is_newer('1.B', '1.A')}")
assert is_newer("1.B", "1.A")

# Geavanceerde Asserties (Alpha/Beta/Prod)
# Beta (-5) is nieuwer dan Alpha (-10)
print(f"is_newer('1.0-beta', '1.0-alpha') = {is_newer('1.0-beta', '1.0-alpha')}")
assert is_newer("1.0-beta", "1.0-alpha")

# Versie 1.0 (impliciet 0) is nieuwer dan 1.0-beta (-5)
print(f"is_newer('1.0', '1.0-beta') = {is_newer('1.0', '1.0-beta')}")
assert is_newer("1.0", "1.0-beta")

# Production (1) is nieuwer dan Development (-20)
print(f"is_newer('app-production', 'app-development') = {is_newer('app-production', 'app-development')}")
assert is_newer("app-production", "app-development")

# Datum (ISO formaat werkt omdat het getallen zijn)
print(f"is_newer('2024.01.01', '2023.12.31') = {is_newer('2024.01.01', '2023.12.31')}")
assert is_newer("2024.01.01", "2023.12.31")

print("\nAlle asserts geslaagd!")

