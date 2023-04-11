#import import_data as import timeit
#from cell import Cell
from astar import AStar
import argparse
import timeit
from bot_utils import import_data, write_to_text, convert_list_to_string, change_status_json


def get_objects_from_data(data):
    obstacle_lst = data['obstacles']
    bot_lst = data['bots']
    start1 = bot_lst[0]['pos']
    start2 = bot_lst[1]['pos']
    status = bot_lst[0]['status']
    coin = data['coin']
    grid_height = data['height']
    grid_width = data['width']
    #initialize grid
    grid = []
    for row in range(grid_height):
        a = []
        for col in range(grid_width):
            a.append(0)
        grid.append(a)
    #initialize obstacle in the grid
    for item in obstacle_lst:
        i = item[0]
        j = item[1]
        grid[i][j] = -1
    #initialize coin in the grid
    i = coin[0]
    j = coin[1]
    grid[i][j] = 'x'
    #initialize bot in the grid
    i = start1[0]
    j = start1[1]
    grid[i][j] = 's1'
    i = start2[0]
    j = start2[1]
    grid[i][j] = 's2'
    bot_1 = bot_lst[0]['name']
    bot_2 = bot_lst[1]['name']
    return {"start_1": start1,
            "start_2": start2,
            "bot_1": bot_1,
            "bot_2": bot_2,
            "coin": coin,
            "grid": grid,
            "status": status}

def locate_midpoint(width, height, obstacles):
    midpoint = [round(width/2), round(height/2)]
    if midpoint in obstacles:
        for i in range(width):
            new_midpoint = [midpoint[0]+1, midpoint[1]]
            if new_midpoint not in obstacles: 
                return new_midpoint
            new_midpoint = [midpoint[0], midpoint[1]+1]
            if midpoint not in obstacles:
                 return new_midpoint
    return midpoint

def convert_to_step(path, start_time):
    convertedPath = []
    for idx, step in list(enumerate(path)):
        if step == path[-1]:
            break
        # current [3, 2] vs [4, 2]
        if step[0] < path[idx+1][0]:
            stop_time = timeit.default_timer()
            convertedPath.append(["down", (stop_time - start_time)*1000])
        if step[0] > path[idx+1][0]:
            stop_time = timeit.default_timer()
            convertedPath.append(["up", (stop_time - start_time)*1000])
        # [3, 2] vs [3,3]
        if step[1] < path[idx+1][1]:
            stop_time = timeit.default_timer()
            convertedPath.append(["right", (stop_time - start_time)*1000])
        if step[1] > path[idx+1][1]:
            stop_time = timeit.default_timer()
            convertedPath.append(["left", (stop_time - start_time)*1000])
    return convertedPath
    
def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help="Input file name")
    parser.add_argument('-o', type=str, help="Output file name")
    args = parser.parse_args()
    return str(args.i), str(args.o)

def run_bot_strategy(input_file):
    data = import_data(input_file)
    objects = get_objects_from_data(data)
    our_bot_path = AStar(objects["bot_1"], objects["start_1"], objects["coin"]).find_shortest_path(objects["grid"])
    return our_bot_path

def run_bot_onestep():
    start_time = timeit.default_timer()
    input_file, output_file = run_cli() 
    data = import_data(input_file)
    objects = get_objects_from_data(data)
    our_bot_path = AStar(objects["bot_1"], objects["start_1"], objects["coin"]).find_shortest_path(objects["grid"])
    our_bot_step = convert_to_step(our_bot_path, start_time)
    print("running...")
    while our_bot_step:
        data = import_data(input_file)
        if data["bots"][0]["status"] == "move":
            one_step = convert_list_to_string(our_bot_step[0])
            print(one_step)
            write_to_text(one_step, one_line = True, filename=output_file)
            our_bot_step.pop(0)
            change_status_json("stop", input_file)
            
        
    print("we found it")

#python bot.py -i maze_metadata.json -o action.txt

if __name__ == "__main__":
   run_bot_onestep()
        

        





