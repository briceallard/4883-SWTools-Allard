import os
import sys
import json
from pprint import pprint

# open read/write paths
read_path = os.path.dirname(os.path.abspath(__file__)) + '/data/game_data/'
write_path = os.path.dirname(os.path.abspath(__file__)) + '/data/playerids/'

# create empty object
myPlayers = {}

# loop through all json files
for filename in os.listdir(read_path):
    with open(read_path + filename) as f:
        data = json.load(f)
        # get game data
        for gameid, gamedata in data.items():
            if gameid != "nextupdate":
                #get drivedata
                for driveid, drivedata in gamedata['drives'].items():
                    if driveid != 'crntdrv':
                        #get play data
                        for playid, playdata in drivedata['plays'].items():
                            for players, playerdata in playdata['players'].items():
                                if players != '0':
                                        
                                    myPlayers['playerID'] = players

                                    for element in playerdata:
                                        myPlayers['playerName'] = element['playerName']
                                    
                                    print(gameid)
                                    pprint(myPlayers['playerID'])

    #create new json files from data
    filename = '%s' % (myPlayers['playerID']) + '.json'

    if not os.path.exists(write_path):
        os.makedirs(write_path)

    w = open(write_path + filename, 'w+')
    w.write(json.dumps(myPlayers))
    w.close()

    # wanted json output example
    # players = { playerID : playerName }

f.close()


    # {
    # "2009081351": {
    #     "home": {
    #         "score": {
    #             "1": 3,
    #             "2": 3,
    #             "3": 16,
    #             "4": 3,
    #             "5": 0,
    #             "T": 25
    #         },
    #         "abbr": "PHI",
    #         "to": 0,
    #         "stats": {
    #             "passing": {
    #                 "00-0020305": {
    #                     "name": "A.Feeley",
    #                     "att": 24,
    #                     "cmp": 18,
    #                     "yds": 211,
    #                     "tds": 1,
    #                     "ints": 0,
    #                     "twopta": 1,
    #                     "twoptm": 0
    #                 },
    #                 "00-0011022": {
    #                     "name": "D.McNabb",
    #                     "att": 18,
    #                     "cmp": 11,
    #                     "yds": 103,
    #                     "tds": 0,
    #                     "ints": 0,
    #                     "twopta": 0,
    #                     "twoptm": 0
    #                 }
    #             },
    #             "rushing": {
    #                 "00-0027029": {
    #                     "name": "L.McCoy",
    #                     "att": 10,
    #                     "yds": 55,
    #                     "tds": 0,
    #                     "lng": 16,
    #                     "twopta": 0,
    #                     "twoptm": 0
    #                 },
    #                 "00-0024738": {
    #                     "name": "E.Buckley",
    #                     "att": 8,
    #                     "yds": 23,
    #                     "tds": 1,
    #                     "lng": 6,
    #                     "twopta": 0,
    #                     "twoptm": 0
    #                 },
    #                 "00-0025458": {
    #                     "name": "L.Booker",
