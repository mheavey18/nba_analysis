# import csv
# import json
# import pandas as pd

# pd.read_csv("nba_odds.csv",
#             skiprows=[4, 5, 6, 7])

# with open('nba_odds.csv') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

names_dict = {
    "Atlanta": "ATL",
    "Boston": "BOS",
    "Brooklyn": "BKN",
    "Charlotte": "CHA",
    "Chicago": "CHI",
    "Cleveland": "CLE",
    "Dallas": "DAL",
    "Denver": "DEN",
    "Detroit": "DET",
    "GoldenState": "GS",
    "Houston": "HOU",
    "Indiana": "IND",
    "LALakers": "LAL",
    "LAClippers": "LAC",
    "Memphis": "MEM",
    "Miami": "MIA",
    "Milwuakee": "MIL",
    "Minnesota": "MIN",
    "NewOrleans": "NO",
    "NewYork": "NY",
    "OklahomaCity": "OKC",
    "Orlando": "ORL",
    "Philidelphia": "PHI",
    "Phoenix": "PHX",
    "Portland": "POR",
    "Sacramento": "SAC",
    "SanAntonio": "SA",
    "Toronto": "TOR",
    "Utah": "UTA",
    "Washington": "WAS"
}

# columns
# id, date, team1 (home), team2, score1, score2, vegas_spread (team1), money_line, over/under, elo_prob1, raptor_prob1, elo_spread, raptor_spread

print(names["Sacramento"])
