from bot import Bot
import json
import time
import timeit
import argparse
from bot_utils import *
from map import *
grid = Map()
data = import_dt(input_file)
index1 = get_bot_index(data, 'tadao')
index2 = get_bot_index(data, 'top')
end = data['coin']
top = Bot(data['bots'][index2]['name'], data['bots'][index2]['pos'], end, data['bots'][index2]['status'], data['bots'][index2]['score'], grid)
while True:
    data = import_dt(input_file)
    grid = Map()
    top.status = data['bots'][index2]['status']
    end = import_dt(input_file)['coin']
    tadao = Bot(data['bots'][index1]['name'], data['bots'][index1]['pos'], end, data['bots'][index1]['status'], data['bots'][index1]['score'], grid)
    top = Bot(data['bots'][index2]['name'], data['bots'][index2]['pos'], end, data['bots'][index2]['status'], data['bots'][index2]['score'], grid)
    top.check_other(tadao)
    path_top = top.find_path()
    if path_top == top.end.coor():
        top.write_to_json(index2)
        continue
    if top.status == "move" and len(path_top) >= 2:
        print(path_top[-1])
        print(path_top[-2])
        top.move(path_top[-1],path_top[-2])
        print(top.stop_time)
        print(top.stop_time - top.start_time)
        top.write_to_json(index2)
    
        
