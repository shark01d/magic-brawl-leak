from Packets.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand

class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.commandID = commandID

    def encode(self):

        commands = {
            203: LogicGiveDeliveryItemsCommand
        }

        if self.commandID in commands:

            self.writeVInt(self.commandID)
            commands[self.commandID].encode(self)
        else:
            print(f"{Helpers.yellow}[SERVER] Cannot create command! ID: {self.commandID}")