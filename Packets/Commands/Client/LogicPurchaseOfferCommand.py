from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand
from Packets.Commands.Server.Add import LogicBuySkinOrBrawler
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
from Database.DatabaseManager import DataBase
from Logic.Shop import Shop

from Utils.Reader import BSMessageReader

class LogicPurchaseOfferCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.offer_index = self.read_Vint()


    def process(self):
        id = Shop.offers[self.offer_index]['ID']
        type = Shop.offers[self.offer_index]['ShopType']
        cost = Shop.offers[self.offer_index]['Cost']
        multiplier = Shop.offers[self.offer_index]['Multiplier']

        def res(type):
            if type == 0 or type == 2:
                newGems = self.player.gems - cost
                self.player.gems = newGems
                DataBase.replaceValue(self, 'gems', newGems)
            elif type == 3:
                newStarPoints = self.player.star_points - cost
                self.player.star_points = newStarPoints
                DataBase.replaceValue(self, 'starpoints', newStarPoints)

        if id in [0, 6, 10, 14]:

            if id in [0, 6]:
                self.player.box_id = 5

            elif id == 14:
                self.player.box_id = 4

            elif id == 10:
                self.player.box_id = 3

            res(type)

            LogicBoxDataCommand(self.client, self.player).send()
        elif id == 3:
        	LogicBuySkinOrBrawler(self.client, self.player, 1, Shop.offers[self.offer_index]['BrawlerID']).send()
        elif id == 4:
        	LogicBuySkinOrBrawler(self.client, self.player, 9, Shop.offers[self.offer_index]['SkinID']).send()
        if id == 16:
        	self.player.gems += multiplier          
        	OutOfSyncMessage(self.client, self.player, f'Claiming offer with type {id} is not supported yet').send()
        if id == 9:
        	self.player.tokensdoubler += multiplier          
        	OutOfSyncMessage(self.client, self.player, f'Claiming offer with type {id} is not supported yet').send()
        if id == 1:
        	self.player.gold += multiplier          
        	OutOfSyncMessage(self.client, self.player, f'Claiming offer with type {id} is not supported yet').send()
        	
        if id == 6 and land == True:
        	DataBase.replaceValue(self, 'starki', 1)       
        	OutOfSyncMessage(self.client, self.player, f'Claiming offer with type {id} is not supported yet').send()
        	
        DataBase.replaceValue(self, 'gems', self.player.gems)
        DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
        DataBase.replaceValue(self, 'gold', self.player.gold)    

