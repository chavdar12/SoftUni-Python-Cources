from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []  # list will contain objects

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for this_guy in self.__players:
            if this_guy.name == player_name:
                self.__players.remove(this_guy)
                return this_guy
        return f"Player {player_name} not found"
