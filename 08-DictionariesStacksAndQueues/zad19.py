import json

with open("students.json") as f:
    file = json.load(f)

with open("limited.json", "w") as limit:
    dict = []
    for line in file:
        dict_line = {}
        dict_line["first_name"] = line["first_name"]
        dict_line["last_name"] = line["last_name"]
        dict_line["id"] = line["id"]

        dict.append(dict_line)

    json.dump(dict, limit)



    
