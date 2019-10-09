# --------------------------------------
# CSCI 127, Lab 4
# September 26, 2017
# Austin Hull
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    max_wins = int(points_earned / 3)
    for max_wins in range(max_wins, -1, -1):
        games_left = games_played - max_wins
        ties = 0
        for games_left in range(games_left):
            ties = points_earned - (max_wins * 3)
        losses = games_played - (max_wins + ties)
        if losses >= 0:
            print(max_wins,"-",ties,"-",losses)
    print()
# --------------------------------------

def process_seasons(seasons):
    season = 0
    for season in range(len(seasons)):
        games_played = seasons[season][0]
        points_earned = seasons[season][1]
        season += 1
        process_season(season, games_played, points_earned)

# --------------------------------------

# format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]

process_seasons(soccer_seasons)

