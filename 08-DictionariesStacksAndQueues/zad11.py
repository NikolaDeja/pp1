import json

movie = {
    "title":"Divergent",
    "year": 2014,
    "actor":{"leading": "Shailene Woodley","supporting": "Theo James"},
    "oscar":False,
}

file = json.dump(movie, open("favourite.json","w"), indent=4)