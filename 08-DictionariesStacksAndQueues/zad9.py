countries = [
    {"name":"Poland", "population":38000000},
    {"name":"USA", "population":331000000},
    {"name":"Brazil", "population":214000000},
    {"name":"Spain", "population":47000000},
    {"name":"Italy", "population":59000000},
    ]
print("COUNTRY POPULATION")
i=0
while i<len(countries):
    country= countries[i]
    print(country["name"], end=" ")
    print(country["population"])
    i+=1
