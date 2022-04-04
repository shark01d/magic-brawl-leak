from Database.DatabaseManager import DataBase
from Utils.Writer import Writer
class LogicBuySkinOrBrawler(Writer):

    def __init__(self, client, player, boxtype, reqID):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.reward = boxtype
        self.reqID = reqID

    def encode(self):
    	print("24111 send")
    	self.writeVint(203)
    	self.writeVint(0)
    	self.writeVint(1)
    	self.writeVint(100)
    	#box header end
    	
    	#reward info start
    	self.writeVint(1)
    	self.writeVint(1)
    	if self.reward == 1:
    		self.player.BrawlersUnlockedState[str(self.reqID)]=1
    		DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
    		self.writeScId(16,self.reqID)
    	else:
    		self.writeVint(0)
    	self.writeVint(self.reward)
    	if self.reward == 9:
    		self.writeScId(29, self.reqID)
    	else:
    		self.writeVint(0)
    	self.writeVint(0)
    	self.writeVint(0)
    	self.writeVint(0)
    	for i in range(13):
    		self.writeVint(0)