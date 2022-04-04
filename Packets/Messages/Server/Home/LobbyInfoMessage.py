from Utils.Writer import Writer

class LobbyInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.player = player

    def encode(self):
        self.writeVint(449)
        self.writeString("Kavmi Shluha\nKavmi Shluha\nKavmi Shluha\nKavmi Shluha\nKavmi Shluha\nKavmi Shluha\nKavmi Shluha\nKavmi Shluha\n")

        self.writeVint(0) # array
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
