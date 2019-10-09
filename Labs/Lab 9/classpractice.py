# “Stranger Things” is the title of the series.
# “The Duffer Brothers” is the creator of the series.
# 1 is the number of seasons that the series has run.
# 8 is the number of episodes that the series contains.
class Series:
    def __init__(self, title, director, seasons, episodes):
        self.title = title
        self.director = director
        self.seasons = seasons
        self.episodes = episodes

    def get_title(self):
        return self.title

    def get_seasons(self):
        return self.seasons

    def get_episodes(self):
        return self.episodes

    def addSeason(self):
        self.seasons += 1

    def addEpisodes(self, number):
        self.episodes += number

    def __str__(self):
        return(str(self.title) + " has aired " + str(self.episodes) +
               " episodes over " + str(self.seasons) + " seasons")
    

stranger_things = Series("Stranger Things", "The Duffer Brothers", 1, 8)

print(stranger_things)
stranger_things.addSeason()         # here comes the next season
stranger_things.addEpisodes(9)      # there are now 9 more episodes
print(stranger_things)

