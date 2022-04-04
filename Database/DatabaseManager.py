from Logic.Player import Players
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@freezzbrawl-shard-00-00.egox9.mongodb.net:27017,freezzbrawl-shard-00-01.egox9.mongodb.net:27017,freezzbrawl-shard-00-02.egox9.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-nwzmpn-shard-0&authSource=admin&retryWrites=true&w=majority', 27017)
db = client['server_v29']

accounts = db['accounts']
gamerooms = db['gamerooms']
clubs = db['clubs']

class DataBase:
    def loadAccount(self):
        user_data = accounts.find_one({'token': self.player.token})
        if user_data:
            self.player.skins = user_data["skins"]
            self.player.theme_id = user_data["theme_id"]
            self.player.name = user_data["name"]
            self.player.low_id = user_data["lowID"]
            self.player.IsFacebookLinked = user_data["isFBLinked"]
            self.player.FacebookID = user_data["facebookID"]
            self.player.club_low_id = user_data["clubID"]
            self.player.club_role = user_data["clubRole"]
            self.player.tutorial = user_data["tutorial"]
            self.player.trophy_road = user_data["leagueReward"]
            self.player.player_experience = user_data["playerExp"]
            self.player.collected_experience = user_data["cappedExp"]
            self.player.solo_wins = user_data["soloWins"]
            self.player.duo_wins = user_data["duoWins"]
            self.player.ThreeVSThree_wins = user_data["3vs3Wins"]
            self.player.gems = user_data["gems"]
            self.player.gold = user_data["gold"]
            self.player.star_points = user_data["starpoints"]
            self.player.tickets = user_data["tickets"]
            self.player.tokensdoubler = user_data["tokensdoubler"]
            self.player.battle_tokens = user_data["availableTokens"]
            self.player.brawler_id = user_data["brawlerID"]
            self.player.skin_id = user_data["skinID"]
            self.player.profile_icon = user_data["profileIcon"]
            self.player.brawl_boxes = user_data["brawlBoxes"]
            self.player.big_boxes = user_data["bigBoxes"]
            self.player.brawlers_skins = user_data["brawlersSkins"]
            self.player.name_color = user_data["namecolor"]
            self.player.gadget = user_data["gadget"]
            self.player.starpower = user_data["starpower"]
            self.player.DoNotDistrubMessage = user_data["DoNotDistrub"]
            self.player.room_id = user_data["roomID"]
            self.player.brawlers_trophies_in_rank = user_data["brawlersTrophiesForRank"]
            self.player.brawlers_upgradium = user_data["brawlersUpgradePoints"]
            self.player.Brawler_level = user_data["brawlerPowerLevel"]
            self.player.Brawler_starPower = user_data["brawlerStarPower"]
            self.player.Brawler_newTag = user_data["brawlerNewTag"]
            self.player.brawlers_trophies = user_data["brawlersTrophies"]            
            if self.player.UnlockType == "Off":
                self.player.BrawlersUnlockedState = user_data["UnlockedBrawlers"]

            player_total_trophies = 0
            for BrawlerID in self.player.brawlers_trophies.keys():
                player_total_trophies += self.player.brawlers_trophies[BrawlerID]
            self.player.trophies = player_total_trophies
            DataBase.replaceValue(self, 'trophies', self.player.trophies)

            if self.player.trophies < user_data["highesttrophies"]:
                self.player.highest_trophies = user_data["highesttrophies"]
            else:
                self.player.highest_trophies = self.player.trophies
                DataBase.replaceValue(self, 'highesttrophies', self.player.highest_trophies)

    def createAccount(self):
        Players.CreateNewBrawlersList()
        data = {
            "theme_id": self.player.theme_id,
            "skins": self.player.skin,
            "token": str(self.player.token),
            "name": self.player.name,
            "lowID": self.player.low_id,
            "clubID": 0,
            "clubRole": 0,
            "isFBLinked": 0,
            "facebookID": self.player.FacebookID,
            "tutorial": self.player.tutorial,
            "leagueReward": self.player.trophy_road,
            "playerExp": self.player.player_experience,
            "cappedExp": self.player.collected_experience,
            "soloWins": self.player.solo_wins,
            "duoWins": self.player.duo_wins,
            "3vs3Wins": self.player.ThreeVSThree_wins,
            "gems": self.player.gems,
            "gold": self.player.gold,
            "starpoints": self.player.star_points,
            "tokensdoubler": self.player.tokensdoubler,
            "availableTokens": self.player.battle_tokens,
            "tickets": self.player.tickets,
            "brawlerID": 0,
            "skinID": 0,
            "trophies": self.player.trophies,
            "highesttrophies": self.player.trophies,
            "profileIcon": 0,
            "namecolor": self.player.name_color,
            "brawlBoxes": self.player.brawl_boxes,
            "bigBoxes": self.player.big_boxes,
            "gadget": 255,
            "starpower": 76,
            "DoNotDistrub": 0,
            "roomID": 0,
            "brawlersSkins": self.player.brawlers_skins,
            "brawlersTrophies": self.player.brawlers_trophies,
            "brawlersTrophiesForRank": self.player.brawlers_trophies_in_rank,
            "brawlersUpgradePoints": self.player.brawlers_upgradium,
            "brawlerPowerLevel": self.player.Brawler_level,
            "brawlerStarPower": self.player.Brawler_starPower,
            "brawlerNewTag": self.player.Brawler_newTag,
            "UnlockedBrawlers": self.player.BrawlersUnlockedState,
        }
        accounts.insert_one(data)

    def getAllPlayers(self):
        return list(accounts.find())

    def getSpecifiedValue(self, value_name):
        account = accounts.find_one({'token': self.token})
        self.requested_val = account[value_name]

    def replaceValue(self, value_name, new_value):
        accounts.update_one(
            {'token': self.player.token},
            {'$set': {value_name: new_value}}
        )

    # Gameroom
    def createGameroomDB(self):
        data = { 
            "room_id": self.player.room_id,
            "mapID": self.player.map_id,
            "useGadget": 1,
            "players": {
                        str(self.player.low_id): {
                        "host": 1,
                        "lowID": self.player.low_id,
                        "name": self.player.name,
                        "Team": self.player.team,
                        "Ready": self.player.isReady,
                        "brawlerID": self.player.brawler_id,
                        "starpower": self.player.starpower,
                        "gadget": self.player.gadget,
                        "profileIcon": self.player.profile_icon,
                        "namecolor": self.player.name_color
                    }
                }
        }
        gamerooms.insert_one(data)

    def loadGameroom(self):
        gameroom_data = gamerooms.find_one({'room_id': self.player.room_id})

        if gameroom_data:
            self.mapID = gameroom_data["mapID"]
            self.useGadget = gameroom_data["useGadget"]
            self.playersdata = {}
            for low_id, info in gameroom_data["players"].items():
                self.playersdata[low_id] = {}
                self.playersdata[low_id]["IsHost"] = info["host"]
                self.playersdata[low_id]["name"] = info["name"]
                self.playersdata[low_id]["Team"] = info["Team"]
                self.playersdata[low_id]["Ready"] = info["Ready"]
                self.playersdata[low_id]["LowID"] = info["lowID"]
                self.playersdata[low_id]["profileIcon"] = info["profileIcon"]
                self.playersdata[low_id]["namecolor"] = info["namecolor"]
                self.playersdata[low_id]["brawlerID"] = info["brawlerID"]
                self.playersdata[low_id]["starpower"] = info["starpower"]
                self.playersdata[low_id]["gadget"] = info["gadget"]

            self.playerCount = len(self.playersdata)
        else:
            DataBase.replaceValue(self, 'roomID', 0)
            self.player.room_id = 0

    def replaceGameroomValue(self, value_name, new_value, type):
        gameroom_data = gamerooms.find_one({'room_id': self.player.room_id})

        if gameroom_data is None:
            DataBase.replaceValue(self, 'room_id', 0)
            return

        if type == "room" or type == "player":
            gamerooms.update_one(
            {'room_id': self.player.room_id},
            {'$set': {str(value_name): new_value}}
        )
        #elif type == "removePlayer":
        #    if gameroom_data["info"][str(new_value)]["host"] == 1:
        #        db.remove(query.room_id == self.player.room_id)
        #    else:
        #        db.remove(query.room_id.any(valueToRemove == str(new_value)))
        else:
            gamerooms.remove({'room_id': self.player.room_id})
    
    def UpdateGameroomPlayerInfo(self, low_id):
        gameroom_data = gamerooms.find_one({'room_id': self.player.room_id})

        gameroom_data["players"][str(low_id)]["Team"] = self.player.team
        gameroom_data["players"][str(low_id)]["Ready"] = self.player.isReady
        gameroom_data["players"][str(low_id)]["brawlerID"] = self.player.brawler_id
        gameroom_data["players"][str(low_id)]["starpower"] = self.player.starpower
        gameroom_data["players"][str(low_id)]["gadget"] = self.player.gadget
        gameroom_data["players"][str(low_id)]["profileIcon"] = self.player.profile_icon
        gameroom_data["players"][str(low_id)]["namecolor"] = self.player.name_color

        gamerooms.update_one({'room_id': self.player.room_id}, {'$set': gameroom_data})

    def createClub(self, clubid):
        data = {
            "clubID": clubid,
            "name": self.clubName,
            "description": self.clubdescription,
            "region": "RU",
            "badgeID": self.clubbadgeID,
            "type": self.clubtype,
            "trophiesneeded": self.clubtrophiesneeded,
            "friendlyfamily": self.clubfriendlyfamily,
            "trophies": self.player.trophies,
            "members": {
                str(self.player.low_id): self.player.name
            },
            "chat": {
                "1": {
                    "Event": 2,
                    "Tick": 1,
                    "PlayerID": self.player.low_id,
                    "PlayerName": self.player.name,
                    "PlayerRole": 2,
                    "Message": "Добро пожаловать в клуб! Введите /Помощь для списка команд."
                }
            }
        }
        clubs.insert_one(data)

    def CountClub(self, minMembers, maxMembers, clubType, maxListLength):
        self.club_list = []
        self.club_data = []
        self.AllianceCount = 0

        for club in clubs.find():
            if self.AllianceCount == maxListLength:
                break
            if minMembers <= len(club['members']) < maxMembers and club['type'] <= clubType:
                self.club_list.append(club['clubID'])
                self.club_data.append(club)
                self.AllianceCount += 1
    
    def loadClub(self, clubid):
        club_data = clubs.find_one({'clubID': clubid})
        self.plrids = []
        self.clubName = club_data["name"]
        self.clubdescription = club_data["description"]
        self.clubregion = club_data["region"]
        self.clubbadgeID = club_data["badgeID"]
        self.clubtype = club_data["type"]
        self.clubtrophiesneeded = club_data["trophiesneeded"]
        self.clubfriendlyfamily = club_data["friendlyfamily"]
        self.clubtrophies = club_data["trophies"]
        self.clubmembercount = len(club_data["members"])
        for plridentifier, data in club_data["members"].items():
            if plridentifier != "totalmembers":
                self.plrids.append(int(plridentifier))

    def AddMember(self, AllianceID, PlayerID, PlayerName, Action):
        data = clubs.find_one({'clubID': AllianceID})

        if Action == 0:
            clubs.remove({'clubID': AllianceID})

        elif Action == 1:
            data['members'][str(PlayerID)] = PlayerName
            clubs.replace_one({'clubID': AllianceID}, data)
            accounts.update_one({'low_id': PlayerID}, {'$set': {'clubID': AllianceID, 'clubRole': 1}})

        elif Action == 2:
            try:
                data['members'].pop(str(PlayerID))
                clubs.replace_one({'clubID': AllianceID}, data)
                accounts.update_one({'low_id': PlayerID}, {'$set': {'clubID': 0, 'clubRole': 0}})
            except:
                pass

    def GetMemberData(self, Low_id):
        try:
            self.players = DataBase.getAllPlayers(self)
            for i in range(len(self.players)):
                if self.players[i]['lowID'] == int(Low_id):
                    self.lowplrid = self.players[i]['lowID']
                    self.plrrole = self.players[i]["clubRole"]
                    self.plrtrophies = self.players[i]["trophies"]
                    self.plrname = self.players[i]["name"]
                    self.plricon = self.players[i]["profileIcon"]
                    self.plrnamecolor = self.players[i]["namecolor"]
                    self.plrexperience = self.players[i]["playerExp"]
                    break
        except Exception as e:
            self.lowplrid = 1
            self.plrrole = 2
            self.plrtrophies = 0
            self.plrname = "Bot"
            self.plricon = 1
            self.plrnamecolor = 2
            self.plrexperience = 0

    def replaceClubValue(self, target, inf1, inf2, inf3, inf4, inf5):
        club_data = clubs.find_one({'clubID': target})

        club_data['description'] = inf1
        club_data['badgeID'] = inf2
        club_data['type'] = inf3
        club_data['trophiesneeded'] = inf4
        club_data['friendlyfamily'] = inf5

        clubs.replace_one({'clubID': target}, club_data)

    def GetmsgCount(self, clubID):
        self.MessageCount = len(clubs.find_one({'clubID': clubID})['chat'])

    def Addmsg(self, clubID, event, tick, Low_id, name, role, msg):
        data = clubs.find_one({'clubID': clubID})
        tick = len(data['chat']) + 1

        data['chat'][str(tick)] = {
            "Event": event,
            "Tick": tick,
            "PlayerID": Low_id,
            "PlayerName": name,
            "PlayerRole": role,
            "Message": msg,
        }
        clubs.replace_one({'clubID': clubID}, data)
