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
    #print(tadao.find_path())
    tadao.check_other(top)
    tadao.dodge_other(top)
    path_tadao = tadao.find_path()

    if path_tadao == tadao.end.coor():
        tadao.write_to_json(input_file, index1)
        continue
    if path_tadao == None:
        tadao.write_to_json(input_file, index1)
        continue
    if tadao.status == "move":
        tadao.move(path_tadao[-1],path_tadao[-2])
        tadao.write_to_json(input_file, index1)

        
