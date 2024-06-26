class Games:
    def __init__(self, max_player_count, game_mode):
        self.max_player_count = max_player_count
        self.game_mode = game_mode

    def getMaxPlayerCount(self):
        print(self.max_player_count)
    def getGame_mode(self):
        print(self.game_mode)


class VideoGames(Games):
    def __init__(self, max, mode):
        super().__init__(max_player_count= max,game_mode= mode)
        self.controller = "keyboard"
    def getControllerType(self):
        print(self.controller)

class BoardGames(Games):
    def __init__(self, mode):
        super().__init__(max_player_count= 4, game_mode= mode)
        self.game_pieces = ["horse", "car", "hat", "dog"]

    def getGame_pieces(self):
        print(self.game_pieces)

games = Games(4,"Co-op")
games.getGame_mode()

board = BoardGames("multiplayer")
board.getGame_pieces()
board.getMaxPlayerCount()

video = VideoGames(1,"Single-player")
video.getControllerType()
video.getGame_mode()
video.getMaxPlayerCount()