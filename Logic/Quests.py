class Quests:
    """
    << Mission Type List >>
    
    1 = Win Battle
    2 = Defeat the Enemy 
    3 = Deal Damage
    4 = Heal Health

    
    << Gamemode IDs List >>
    
    0 = Gem Grab
    2 = Heist
    3 = Bounty
    5 = Brawlball
    6 = Solo Showdown
    7 = Big Game
    8 = Robo Rumble
    9 = Duo Showdown
    10 = Boss Fight
    11 = Siege
    14 = Takedown
    15 = Lone Star
    16 = Present Plunder
    
    BP is Brawl Pass
    
    """
    
    
    
    missions = [
    
        {
            'MissionType': 3,
            'QuestType': 0,
            'CurrentGoal': 8923,
            'MaxGoal': 0,
            'TokensReward': 500,
            'CurrentLevel': 99,
            'MaxLevel': 100,
            'BPExclusive': False,
            'BrawlerID': 6,
            'Gamemode': 8
        },
        
    ]
    
    
    def EncodeQuestsMissions(self):
        self.writeBoolean(True) # Quests Boolean
        count = len(Quests.missions)
        self.writeVint(count)
        for i in range(count):
            item = Quests.missions[i]
            
            self.writeVint(0)
            self.writeVint(0)
            
            self.writeVint(item['MissionType']) # Mission Type
            self.writeVint(item['CurrentGoal']) # Current Quest Goal
            self.writeVint(item['MaxGoal']) # Max Quest Goal
            self.writeVint(item['TokensReward']) # Tokens Reward
            
            self.writeVint(0)
            
            self.writeVint(item['CurrentLevel']) # Current Level 
            self.writeVint(item['MaxLevel']) # Max Level
            
            self.writeVint(item['QuestType']) # Quest Type | 0 = Season Quest, 1 = Daily Quest
            
            self.writeBoolean(item['BPExclusive']) # Brawl Pass Exclusive
            self.writeScId(16, item['BrawlerID']) # Brawler ID
            self.writeVint(item['Gamemode']) # Gamemode ID
            
            self.writeVint(0)
            self.writeVint(0)
