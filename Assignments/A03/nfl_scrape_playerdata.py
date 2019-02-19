import os
import sys
import json
import math
from pprint import pprint

read_path = os.path.dirname(os.path.abspath(__file__)) + '/data/game_data/'
write_path = os.path.dirname(os.path.abspath(__file__)) + '/data/playerdata/'

players = {}
file_read_count = 1
file_total_count = len([f for f in os.listdir(read_path) if os.path.isfile(os.path.join(read_path, f))])

for filename in os.listdir(read_path):
    print("Gathering data - {0} of {1} - {2}%".format(file_read_count, file_total_count, math.trunc(file_read_count / file_total_count * 100)))

    with open(read_path + filename) as f:
        data = json.load(f)

        for game_id, game_data in data.items():
            if game_id != "nextupdate":

                for drive_id, drive_data in game_data['drives'].items():
                    if drive_id != "crntdrv":

                        for play_id, play_data in drive_data['plays'].items():

                            for player_id, player_data in play_data['players'].items():
                                if player_id != "0":
                                    
                                    if player_id not in players.keys():
                                        players[player_id] = {}
                                        players[player_id]['teams'] = []
                                        players[player_id]['stats'] = []

                                    for stat in player_data:
                                        stat['gameId'] = game_id
                                        players[player_id]['playerName'] = stat['playerName']
                                        players[player_id]['stats'].append(stat)

                                        if stat['clubcode'] not in players[player_id]['teams']:
                                            players[player_id]['teams'].append(stat['clubcode'])
    
    file_read_count+=1

    # pprint(players)
    # sys.exit()

for key in players:
    filename = '%s' % (key) + '.json'

    if not os.path.exists(write_path):
        os.makedirs(write_path)

    w = open(write_path + filename, 'w+')
    w.write(json.dumps(players[key]))
    w.close()

f.close()
