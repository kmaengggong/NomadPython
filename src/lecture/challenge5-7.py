class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello, I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
    
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def show_player(self):
        print(f"Introducing from {self.team_name}:")
        for player in self.players:
            player.introduce()

    # Challenge1: delete method
    def delete_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                return
            
    # Challenge2: show total xp method
    def show_total_xp(self):
        xp = 0
        for player in self.players:
            xp += player.xp
        print(f"{self.team_name}'s xp: {xp}")

team_tt = Team("Togenashi Togeari")
team_dd = Team("Diamond Dust")

team_tt.add_player("Nina")
team_dd.add_player("Momoka")

team_tt.show_player()
team_dd.show_player()

team_dd.delete_player("Momoka")
team_dd.add_player("Hina")
team_tt.add_player("Momoka")

team_tt.show_player()
team_dd.show_player()

team_tt.show_total_xp()
team_dd.show_total_xp()