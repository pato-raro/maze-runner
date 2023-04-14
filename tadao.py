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
tadao = Bot(data['bots'][index1]['name'], data['bots'][index1]['pos'], end, data['bots'][index1]['status'], data['bots'][index1]['score'], grid)
while True:
    data = import_dt(input_file)
    grid = Map()
    tadao.status = data['bots'][index1]['status']
    end = data['coin']
    tadao = Bot(data['bots'][index1]['name'], data['bots'][index1]['pos'], end, data['bots'][index1]['status'], data['bots'][index1]['score'], grid)
    top = Bot(data['bots'][index2]['name'], data['bots'][index2]['pos'], end, data['bots'][index2]['status'], data['bots'][index2]['score'], grid)
    tadao.check_other(top)
    path_tadao = tadao.find_path()
    if path_tadao == tadao.end.coor():
        tadao.write_to_json(index1)
        continue
    if tadao.status == "move" and len(path_tadao) >= 2:
        tadao.move(path_tadao[-1],path_tadao[-2])
        print(tadao.stop_time)
        print(tadao.stop_time - tadao.start_time)
        tadao.write_to_json(index1)

        
