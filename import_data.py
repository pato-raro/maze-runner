import json
f = open("maze_metadata.json")
with open("maze_metadata.json", 'r') as file:
    data = json.load(file)
    #print(data)