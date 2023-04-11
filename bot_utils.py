import json

def import_data(location = "maze_metadata.json"):
    f = open(location)
    with open(location, 'r') as file:
        data = json.load(file)
    return data

def write_to_text(context, one_line = True, filename = "action.txt"):
    if one_line:
        f = open(filename, 'a')
        f.write(str(context))
        f.write("\n")
    else:
        f = open(filename, 'w')
        f.write(context)
    f.close()
    
def convert_list_to_string(context):
    return " ".join(list(map(str,context)))

def change_status_json(status, filename = "maze_metadata.json"):
    with open(filename, "r") as jsonFile:
        data = json.load(jsonFile)
    data["bots"][0]["status"] = status
    with open(filename, "w") as jsonFile:
        json.dump(data, jsonFile)
