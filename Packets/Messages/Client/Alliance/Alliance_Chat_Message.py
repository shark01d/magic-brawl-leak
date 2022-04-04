from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage
from Packets.Messages.Server.AllianceBot.Alliance_Bot_Chat_Server_Message import AllianceBotChatServerMessage
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader

class AllianceChatMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False

    def decode(self):
        self.msg = self.read_string()

        if self.msg.lower() == '/инфа':
            self.bot_msg = f'Имя игрока: {self.player.name}, трофеи игрока: {self.player.trophies}, лоу айди игрока: {self.player.low_id}, токен игрока: {self.player.token}'
            self.IsAcmd = True

        elif self.msg.lower() == '/reset':
            self.send_ofs = True
            DataBase.replaceValue(self, 'gold', 99999)
            DataBase.replaceValue(self, 'gems', 99999)
            DataBase.replaceValue(self, 'tickets', 99999)
            self.IsAcmd = False

        elif self.msg.lower().startswith('/gems'):
            try:
                newGems = self.msg.split(" ", 4)[1:]
                DataBase.replaceValue(self, 'gems', int(newGems[0]))
                self.send_ofs = False
                self.IsAcmd = False
            except:
                pass

        elif self.msg.lower().startswith('/gold'):
            try:
                newGold = self.msg.split(" ", 4)[1:]
                DataBase.replaceValue(self, 'gold', int(newGold[0]))
                self.send_ofs = False
                self.IsAcmd = False
            except:
                pass

        elif self.msg.lower().startswith('/tickets'):
            try:
                newTickets = self.msg.split(" ", 7)[1:]
                DataBase.replaceValue(self, 'tickets', int(newTickets[0]))
                self.send_ofs = False
                self.IsAcmd = False
            except:
                pass

        elif self.msg.lower().startswith('/starpoints'):
            try:
                newStarpoints = self.msg.split(" ", 10)[1:]
                DataBase.replaceValue(self, 'starpoints', int(newStarpoints[0]))
                self.send_ofs = False
                self.IsAcmd = False
            except:
                pass

        elif self.msg.lower() == '/help':
            self.bot_msg = 'Club Commands\n/stats - show server status\n/reset - reset all resources\n/gems [int] - add gems to your account, where int is the number of gems\n/gold [int] - add gold to your account, where int is the number of gold\n/tickets [int] - add tickets to your account, where int is the number of tickets\n/starpoints [int] - add starpoints to your account, where int is the number of starpoints'
            self.IsAcmd = True
            
            self.msg = self.read_string()

        if self.msg.lower() == '/test':
            self.bot_msg = f'Ресурсы игрока: монеты: {self.player.gold}, билеты: {self.player.tickets} старпоинты: {self.player.star_points}, гемы: {self.player.gems}'
            self.IsAcmd = True
            
            self.msg = self.read_string()

        if self.msg.lower() == '/theme id':
            self.bot_msg = f'Помощь по темам в меню (0-11):\n0 - дефолтная тема\n1 - дефолтная тема со снегом\n2 - лунный новый год тема\n3 - клэш рояль тема\n4 - ???\n5 - золотая неделя\n6 - ретрополис тема\n7 - меха тема\n8 - хэллоуин тема\n9 - бравлидейс тема\n10 - аркадная тема\n11 - футбольная тема'
            self.IsAcmd = True
            
        elif self.msg.lower().startswith('/theme'):
            try:
                newDudka = self.msg.split(" ", 4)[1:]
                DataBase.replaceValue(self, 'theme_id', int(newDudka[0]))
                self.send_ofs = True
                self.IsAcmd = True
            except:
                pass

    def process(self):
        if self.send_ofs == False and self.IsAcmd == False:
            DataBase.Addmsg(self, self.player.club_low_id, 2, 0, self.player.low_id, self.player.name, self.player.club_role, self.msg)
            DataBase.loadClub(self, self.player.club_low_id)
            for i in self.plrids:
                AllianceChatServerMessage(self.client, self.player, self.msg).sendWithLowID(i)

        if self.bot_msg != '':
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send()

        if self.send_ofs:
            OutOfSyncMessage(self.client, self.player, 'Changes have been applied').send()