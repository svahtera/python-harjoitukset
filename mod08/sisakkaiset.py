autot=[
    {
        "merkki": "Toyota",
        "malli": "Corolla",
        "vuosimalli": 2018
    },
    {
        "merkki": "Ford",
        "malli": "Focus",
        "vuosimalli": 2020
    },
    {
        "merkki": "Volkswagen",
        "malli": "ID.3",
        "vuosimalli": 2023
    }
]

#toinen_auto = autot[1]
#print("Toisen auton tiedot:")
#print(toinen_auto)
print("Autojen tiedot:")
for i in autot:
    print(f"{i["merkki"]} {i["malli"]} ({i["vuosimalli"]})")