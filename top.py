from bot import Bot
import json
import time
import timeit
import argparse
from bot_utils import *
from map import *
data = import_dt(input_file)
grid = Map(data)
index1 = get_bot_index(data, 'tadao')
index2 = get_bot_index(data, 'top')
while True:
    data = import_dt(input_file)
    grid = Map(data)
    end = data['coin']
    tadao = Bot(data['bots'][index1]['name'], 
                data['bots'][index1]['pos'], 
                end, 
                data['bots'][index1]['status'], 
                data['bots'][index1]['score'], 
                grid)
    top = Bot(data['bots'][index2]['name'], 
              data['bots'][index2]['pos'], 
              end, 
              data['bots'][index2]['status'], 
              data['bots'][index2]['score'], 
              grid)
    top.check_other(tadao)
    top.dodge_other(tadao)
    path_top = top.find_path()
    if path_top == top.end.coor():
        top.write_to_json(index2)
        continue
    if path_top == None:
        top.write_to_json(index2)
        continue
    if top.status == "move":
        top.move(path_top[-1],path_top[-2])
        time.sleep(0.05)
        top.write_to_json(index2)
    
        
