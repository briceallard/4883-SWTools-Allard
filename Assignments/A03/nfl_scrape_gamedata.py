import os
import sys
import json
import urllib.request
from time import sleep
from beautifulscraper import BeautifulScraper
from pprint import pprint

if len(sys.argv) != 2:

    print('Enter filename to use. Ex. "python3 nfl_scrape_gamedata.py gameids_2009_to_2019.json')

else:

    try:

        read_path = os.path.dirname(os.path.abspath(__file__)) + '/data/gameids/'
        write_path = os.path.dirname(os.path.abspath(__file__)) + '/data/game_data/'
        filename = str(sys.argv[1])

        if not os.path.exists(read_path):
            os.makedirs(read_path)

        with open(read_path + filename) as f:
            data = json.load(f)

        base_url = 'http://www.nfl.com/liveupdate/game-center/'

        for season, subdictionary in data.items():
            # Get preseason games
            if season == 'PRE':
                for year, weeks in subdictionary.items():
                    for week, gameids in weeks.items():
                        for gameid in gameids:
                            try:
                                url = base_url + '%s/%s_gtd.json' % (gameid, gameid)
                                urllib.request.urlretrieve(url, write_path + gameid + '.json')
                                print('Season:', season, 'Year:', year, 'Week:', week, 'GameID:', gameid, '- Downloaded!')
                            except:
                                print('Season:', season, 'Year:', year, 'Week:', week, 'GameID:', gameid, '- 404 Error')
            # get regular season games
            if season == 'REG':
                for year, weeks in subdictionary.items():
                    for week, gameids in weeks.items():
                        for gameid in gameids:
                            try:
                                url = base_url + '%s/%s_gtd.json' % (gameid, gameid)
                                urllib.request.urlretrieve(url, write_path + gameid + '.json')
                                print('Season:', season, 'Year:', year, 'Week:', week, 'GameID:', gameid, '- Downloaded!')
                            except:
                                print('Season:', season, 'Year:', year, 'Week:', week, 'GameID:', gameid, '- 404 Error')
            # get post season games
            if season == 'POST':
                for year, gameids in subdictionary.items():
                    for gameid in gameids:
                        try:
                            url = base_url + '%s/%s_gtd.json' % (gameid, gameid)
                            urllib.request.urlretrieve(url, write_path + gameid + '.json')
                            print('Season:', season, 'Year:', year, 'Week: 1', 'GameID:', gameid, '- Downloaded!')
                        except:
                            print('Season:', season, 'Year:', year, 'Week: 1', 'GameID:', gameid, '- 404 Error')

        print('Game ID import completed successfully')

    except:
        
        print('Enter filename to use. Ex. "python3 nfl_scrape_gamedata.py gameids_2009_to_2019.json')