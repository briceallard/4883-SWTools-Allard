import os
import sys
import json
import math
from pprint import pprint
from collections import OrderedDict
from itertools import islice

# Returns all files in an array
def getFiles(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):

        for filename in filenames:
            files.append(os.path.join(dirname, filename))

        if '.git' in dirnames:
            dirnames.remove('git')
        
        return files

# Try to open file if JSON format
def openFileJson(path):
    try:
      f = open(path, "r")
      data = f.read()
      if isJson(data):
          return json.loads(data)
      else:
          print("Error: Not json.")
          return {}
    except IOError:
        print("Error: Game file doesn't exist.")
        return {}

# Determine if file is Json format
def isJson(filename):
    try:
        file = json.loads(filename)
    except ValueError as e:
        return False
    return True

# Find the player(s) that played for the most teams.
def mostTeamsCareer(files):
    players = {
        'playerName': '',
        'totTeams': 0,
        'teams': []
    }

    for file in files:
        data = openFileJson(file)

        if players['totTeams'] < len(data['teams']):
            players['playerName'] = data['playerName']
            players['totTeams'] = len(data['teams'])
            players['teams'] = data['teams']

    return players

# Find the player(s) that played for multiple teams in one year.
def mostTeamsYear(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                gameId = stat['gameId']

                players[data['playerName']] = {}
                players[data['playerName']]['totTeams'] = 1
                players[data['playerName']]['teams'] = {}
                players[data['playerName']]['teams']['year'] = gameId[:4]
                players[data['playerName']]['teams']['teams'] = []


                if stat['clubcode'] not in players[data['playerName']]['teams']:
                    players[data['playerName']]['teams']['teams'].append(stat['clubcode'])
            
            elif data['playerName'] in players.keys():
                players[data['playerName']]['totTeams'] += 1

                if gameid[:4] not in players[data['playerName']]['teams']['year']:
                    players[data['playerName']]['teams']['year'] = gameId[:4]

            pprint(players)
            sys.exit()

    return players

# Find the player(s) that had the most yards rushed for a loss.
def mostRushYardMinus(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                if stat['statId'] == 10:
                    players[data['playerName']] = {}
                    players[data['playerName']]['totYds'] = stat['yards']
                    players[data['playerName']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 10 and stat['yards'] < 0:
                    players[data['playerName']]['totYds'] += stat['yards']
                    players[data['playerName']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(players, key=lambda x: players[x]['totYds'])

    for key in sorted_keys:
        sorted_dict[key] = players[key]

    top_five = list(islice(sorted_dict.items(), 5))
    return top_five

# Find the player(s) that had the most rushes for a loss.
def mostRushMinus(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                if stat['statId'] == 10:
                    players[data['playerName']] = {}
                    players[data['playerName']]['totYds'] = stat['yards']
                    players[data['playerName']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 10 and stat['yards'] < 0:
                    players[data['playerName']]['totYds'] += stat['yards']
                    players[data['playerName']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(players, key=lambda x: players[x]['count'])

    for key in sorted_keys:
        sorted_dict[key] = players[key]

    top_five = list(islice(sorted_dict.items(), 5))
    return top_five

# Find the player(s) with the most number of passes for a loss.
def mostPassMinus(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                if stat['statId'] == 21:
                    players[data['playerName']] = {}
                    players[data['playerName']]['totYds'] = stat['yards']
                    players[data['playerName']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 21 and stat['yards'] < 0:
                    players[data['playerName']]['totYds'] += stat['yards']
                    players[data['playerName']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(players, key=lambda x: players[x]['count'])

    for key in sorted_keys:
        sorted_dict[key] = players[key]

    top_five = list(islice(sorted_dict.items(), len(sorted_dict) - 5, len(sorted_dict)))
    return top_five
    
# Find the team with the most penalties.
def mostTeamPenalties(files):
    teams = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if stat['clubcode'] not in teams.keys():
                if stat['statId'] == 93:
                    teams[stat['clubcode']] = {}
                    teams[stat['clubcode']]['totYds'] = stat['yards']
                    teams[stat['clubcode']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 93:
                    teams[stat['clubcode']]['totYds'] += stat['yards']
                    teams[stat['clubcode']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(teams, key=lambda x: teams[x]['count'])

    for key in sorted_keys:
        sorted_dict[key] = teams[key]

    top_five = list(islice(sorted_dict.items(), len(sorted_dict) - 5, len(sorted_dict)))
    return top_five

# Find the team with the most yards in penalties.
def mostYardsPenalties(files):
    teams = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if stat['clubcode'] not in teams.keys():
                if stat['statId'] == 93:
                    teams[stat['clubcode']] = {}
                    teams[stat['clubcode']]['totYds'] = stat['yards']
                    teams[stat['clubcode']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 93:
                    teams[stat['clubcode']]['totYds'] += stat['yards']
                    teams[stat['clubcode']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(teams, key=lambda x: teams[x]['totYds'])

    for key in sorted_keys:
        sorted_dict[key] = teams[key]

    top_five = list(islice(sorted_dict.items(), len(sorted_dict) - 5, len(sorted_dict)))
    return top_five

# Find the correlation between most penalized teams and games won / lost.




# Average number of plays in a game.
def averageNumPlays(files):

    for file in files:
        data = openFileJson(file)
 
        games = 0
        plays = 0

        for game_id, game_data in data.items():
            if game_id != 'nextupdate':
                games += 1

                for drive_id, drive_data in game_data['drives'].items():
                    if drive_id != 'crntdrv':
                        plays += drive_data['numplays']

    return plays / games

# Longest field goal.
def longestFieldGoal(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                if stat['statId'] == 70:
                    players[data['playerName']] = {}
                    players[data['playerName']]['totYds'] = stat['yards']

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 70 and players[data['playerName']]['totYds'] < stat['yards']:
                    players[data['playerName']]['totYds'] = stat['yards']

    sorted_dict = OrderedDict()
    sorted_keys = sorted(players, key=lambda x: players[x]['totYds'])

    for key in sorted_keys:
        sorted_dict[key] = players[key]

    top_five = list(islice(sorted_dict.items(), len(sorted_dict) - 5, len(sorted_dict)))
    return top_five

# Most field goals.
def mostFieldGoals(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                if stat['statId'] == 70:
                    players[data['playerName']] = {}
                    players[data['playerName']]['totYds'] = stat['yards']
                    players[data['playerName']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 70:
                    players[data['playerName']]['totYds'] += stat['yards']
                    players[data['playerName']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(players, key=lambda x: players[x]['count'])

    for key in sorted_keys:
        sorted_dict[key] = players[key]

    top_five = list(islice(sorted_dict.items(), len(sorted_dict) - 5, len(sorted_dict)))
    return top_five

# Most missed field goals.
def mostMissedFieldGoals(files):
    players = {}

    for file in files:
        data = openFileJson(file)

        for stat in data['stats']:
            if data['playerName'] not in players.keys():
                if stat['statId'] == 69:
                    players[data['playerName']] = {}
                    players[data['playerName']]['totYds'] = stat['yards']
                    players[data['playerName']]['count'] = 1

            elif stat['statId'] != None and stat['yards'] != None:
                if stat['statId'] == 69:
                    players[data['playerName']]['totYds'] += stat['yards']
                    players[data['playerName']]['count'] += 1

    sorted_dict = OrderedDict()
    sorted_keys = sorted(players, key=lambda x: players[x]['count'])

    for key in sorted_keys:
        sorted_dict[key] = players[key]

    top_five = list(islice(sorted_dict.items(), len(sorted_dict) - 5, len(sorted_dict)))
    return top_five

# Most dropped passes (Search for "pass" and "dropped" in play description, and stat-id 115).





player_path = os.path.dirname(os.path.abspath(__file__)) + '/data/playerdata/'
game_path = os.path.dirname(os.path.abspath(__file__)) + '/data/game_data/'

player_files = getFiles(player_path)
game_files = getFiles(game_path)

# print("\nFind the player(s) that played for the most teams:")
# pprint(mostTeamsCareer(player_files))

print("\nFind the player(s) that played for multiple teams in one year:")
pprint(mostTeamsYear(player_files))

# print("\nFind the player(s) that had the most yards rushed for a loss:")
# pprint(mostRushYardMinus(player_files))

# print("\nFind the player(s) that had the most rushes for a loss:")
# pprint(mostRushYardMinus(player_files))

# print("\nFind the player(s) with the most number of passes for a loss:")
# pprint(mostPassMinus(player_files))

# print("\nFind the team with the most penalties:")
# pprint(mostTeamPenalties(player_files))

# print("\nFind the team with the most yards in penalties:")
# pprint(mostYardsPenalties(player_files))

# print("\nFind the average number of plays in a game:")
# pprint(averageNumPlays(game_files))

# print("\nFind the longest field goal:")
# pprint(longestFieldGoal(player_files))

# print("\nFind the most field goals:")
# pprint(mostFieldGoals(player_files))

# print("\nFind the most missed field goals:")
# pprint(mostMissedFieldGoals(player_files))