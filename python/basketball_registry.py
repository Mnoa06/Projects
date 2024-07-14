# Create a new Python file (e.g., basketball_registry.py).
# Define the Player class with attributes (name, position, year).
# Include a method (display_info) to display player information.

class Player:
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year
        
    def display_info(self):
        return f"{self.name} - {self.position} ({self.year})"
    
# Create the Team class with attributes (name, players).
# Include methods to add players (add_player), display the roster (display_roster), and search for a player (search_player).
# Implement a method (sort_roster) to sort players based on their joining year.

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
        
    def display_roster(self):
        roster_info = f"Roster for {self.name}:\n"
        for player in self.players:
            roster_info += f" - {player.display_info()}\n"
        return roster_info
    
    def search_player(self, player_name):
        for player in self.players:
            if player.name.lower() == player_name.lower():
                return player
        return None
    def sort_roster(self):
            # Sort players by joining year using a simple bubble sort
            n = len(self.players)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if self.players[j].year > self.players[j + 1].year:
                        self.players[j], self.players[j + 1] = self.players[j + 1], self.players[j]
                        
# Create the RegistryManager class 
# with a static method (validate_year) for year validation.
#Include a class method (create_player) to create player 
# instances with validation. 

class RegistryManager:
    @staticmethod
    def validate_year(year):
        if not isinstance(year, int) or year < 1980 or year > 2000:
            raise ValueError("Invalid year. Must be between 1980 and 2020")
    
    @classmethod
    def create_player(cls,name,position, year):
        cls.validate_year(year)
        return Player(name,position,year)
    
# Create an instance of the Team class and use a while loop for the main program.
# Implement user-friendly prompts for input, allowing 
# users to create teams, add players, search for players, display rosters, and exit.  

#MAIN PROGRAM

try:
    teams = []
    
    while True:
        print("\Basketball Registry System")
        print("1. Create a Team")
        print("2. Add Player to Team")
        print("3. Search for Player")
        print("4.Display Team Rosters")
        print("5.Exist")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            team_name = input ("Enter the team name: ")
            new_team = Team(team_name)
            teams.append(new_team)
            print(f"Team '{team_name}' created successfully.")
        
        elif choice  == "2":
            team_name = input("Enter a team name")
            
            #Find the team
            selected_team = None
            for team in teams:
                if team.name.lower() == team_name.lower():
                    selected_team = team
                    break
            if selected_team:
                player_name = input("Enter player name: ")
                position = input("Enter player position: ")
                year = int(input("Enter the joining year: "))
                
                new_player = RegistryManager.create_player(player_name, position, year)
                selected_team.add_player(new_player)
                print(f"Player '{player_name}' added to '{team_name}' successfully")
            else:
                print(f"Team '{team_name} not found.")
                
            
        elif choice == "3":
            player_name = input("Enter player name to search: ")
            
            #Search for the player in all teams
            found_player = None
            for team in teams:
                found_player = team.search_player(player_name)
                if found_player:
                    break
            if found_player:
                (print(f"Player '{player_name}' found: {found_player}"))
            else:
                print(f"Player '{player_name}' not found")
                
        
        elif choice == "4":
            for team in teams:
                team.sort_roster()
                print(team.display_roster())
                
        
        elif choice == "5":
            print("Exiting the Basketball Registry System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a valid option")
            
except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Am unexpexted error has occured: {e}")
    
                
