# Parent Class
class FootballClub:
    def __init__(self, name, stadium, city, founded_year):
        self.name = name                # Club's Name
        self.stadium = stadium          # Home Stadium
        self.city = city                # Club's City
        self.founded_year = founded_year  # Year Club Founded
    
    # Method to display club details
    def display_info(self):
        print(f"Club: {self.name}\nStadium: {self.stadium}\nCity: {self.city}\nFounded: {self.founded_year}")

# Child Class 1 - Top Club
class TopClub(FootballClub):
    def __init__(self, name, stadium, city, founded_year):
        super().__init__(name, stadium, city, founded_year)
    
    # Method for celebrating a win
    def celebrate_win(self):
        print(f"{self.name} celebrates another victory!")

# Child Class 2 - Mid-Table Club
class MidTableClub(FootballClub):
    def __init__(self, name, stadium, city, founded_year):
        super().__init__(name, stadium, city, founded_year)
    
    # Method to express fight for survival
    def fight_for_survival(self):
        print(f"{self.name} is fighting hard to secure their place in the league!")

# Create Objects
liverpool = TopClub("Liverpool", "Anfield", "Liverpool", 1892)
southampton = MidTableClub("Southampton", "St Mary's Stadium", "Southampton", 1885)

# Demonstrate Functionality
print(" Top Club Details:")
liverpool.display_info()
liverpool.celebrate_win()

print("\n Mid-Table Club Details:")
southampton.display_info()
southampton.fight_for_survival()


