## NFL Data Scraping

**Files**
* nfl_stat_ids.json - a list of all the play type id and descriptions of what the plays are.
* nfl_scrape_gamedata.py - Gets all data for games from seasons 2009-2019 and stores the scraped data in /game_data/
* nfl_scrape_gameids.py - Gets all gameid's from the NFL website from seasons 2009-2019 and stores the data in /gameids/
* nfl_scrape_playerdata.py - Gets all data from /playerids/*.json files and stores the data into /playerdata/
* nfl_scrape_playerids - Gets all player id's and stores them in /playerids/
* nfl_analyze_data.py - The main file that gathers all data provided from previous files and answers the questions for the assignment.

## Instructions
**Execute the following commands in the terminal in this order:**
* `python3 nfl_scrape_gameids.py startYear endYear`
