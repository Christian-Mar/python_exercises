

gebruiker = {
    "naam": "Jasper",
    "stad": "Utrecht",
    "leeftijd": 28
}

naam = gebruiker["naam"]
print(f"Naam: {naam}")

land = gebruiker.get("land")
print(f"Land: {land}")


taal = gebruiker.get("taal", "Nederlands")
print(f"Taal: {taal}")

