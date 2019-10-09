# --------------------------------------
# CSCI 127, Lab 6
# October 10, 2017
# Austin Hull
# --------------------------------------

# Change 1: The process_season parameters include output_file 

def process_season(output_file, season, games_played, points_earned):
    output_file.write("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned)+ "\n")
    output_file.write("Possible Win-Tie-Loss Records\n")
    output_file.write("-----------------------------\n")
    max_wins = int(points_earned / 3)
    for max_wins in range(max_wins, -1, -1):
        games_left = games_played - max_wins
        ties = 0
        for games_left in range(games_left):
            ties = points_earned - (max_wins * 3)
        losses = games_played - (max_wins + ties)
        if losses >= 0:
            output_file.write(str(max_wins)+ "-" + str(ties) + "-" + str(losses))
            output_file.write("\n")
    output_file.write("\n")
# --------------------------------------

# Change 2: The process_seasons parameters are input_file (e.g. "soccer-in.txt") and output_file (e.g. "soccer-out.txt")

def process_seasons(input_file, output_file):
    in_file = open(input_file, "r")
    out_file = open(output_file, "w")
    season = 0
    for seasons in in_file:
        seasons = seasons.split()
        games_played = int(seasons[0])
        points_earned = int(seasons[1])
        season += 1
        process_season(out_file, season, games_played, points_earned)
    in_file.close()
    out_file.close()

# --------------------------------------

# Change 3: The function process_seasons is called with "soccer-in.txt" and "soccer-out.txt" 

process_seasons("soccer-in.txt", "soccer-out.txt")
