import os
import sys
import json
from beautifulscraper import BeautifulScraper
from time import sleep
from pprint import pprint

# Get input file from terminal
if len(sys.argv) != 3:

    print('Enter start and end year to run script. Ex. "python3 nfl_scrape_gameids.py 2009 2019"')

else:
    #load scraper data and urls
    bs = BeautifulScraper()

    schedule_url = 'http://www.nfl.com/schedules/'
    game_url = 'http://www.nfl.com/liveupdate/game-center/'

    startYear = int(sys.argv[1])
    endYear = int(sys.argv[2])

    years = [x for x in range(startYear, endYear)]
    preWeeks = [x for x in range(1, 5)]  # to include HOF, make (0,5)
    regWeeks = [x for x in range(1, 18)]
    #postWeeks = Nothing due to web structure. All weeks on one page.

    gameids = {
        'PRE': {},
        'REG': {},
        'POST': {}
    }

    for year in years:
        # update pre-season data
        gameids['PRE'][year] = {}

        print('Gathering Pre-Season for Year: %d' % year)

        for week in preWeeks:
            gameids['PRE'][year][week] = []
            url = schedule_url + '%d/PRE%s' % (year, week)
            print('Week: %s' % week)

            soup = bs.go(url)
            schedules = soup.find_all(
                'div', {'class': 'schedules-list-content'})

            for schedule in schedules:
                gameids['PRE'][year][week].append(schedule['data-gameid'])
                print('.', end='', flush=True)
                sleep(0.02)

            print('')

        # update regular season data
        gameids['REG'][year] = {}

        print('Gathering Reg-Season for Year: %d' % year)

        for week in regWeeks:
            gameids['REG'][year][week] = []
            url = schedule_url + '%d/REG%s' % (year, week)
            print('Week: %s' % week)

            soup = bs.go(url)
            schedules = soup.find_all(
                'div', {'class': 'schedules-list-content'})

            for schedule in schedules:
                gameids['REG'][year][week].append(schedule['data-gameid'])
                print('.', end='', flush=True)
                sleep(0.02)

            print('')

        # update post season data
        gameids['POST'][year] = []

        print('Gathering Post-Season for Year: %d' % year)

        url = schedule_url + '%d/POST' % (year)

        soup = bs.go(url)
        schedules = soup.find_all(
            'div', {'class': 'schedules-list-content'})

        for schedule in schedules:
            gameids['POST'][year].append(schedule['data-gameid'])
            print('.', end='', flush=True)
            sleep(0.02)

        print('')

    # write data to new json file
    path = os.path.dirname(os.path.abspath(__file__)) + '/data/gameids/'
    filename = 'gameids_%s_to_%s' % (startYear, endYear) + '.json'

    if not os.path.exists(path):
        os.makedirs(path)

    f = open(path + filename, 'w+')
    f.write(json.dumps(gameids))
    f.close()

    print('Scrape Complete!')
    print('Saved to /data/gameids/' + filename + '\n')
