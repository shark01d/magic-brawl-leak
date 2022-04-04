class Shop:
    """
    << Shop Offers IDs List >>

    0 = Free Brawl Box
    1 = Gold
    2 = Random Brawler
    3 = Brawler
    4 = Skin
    5 = StarPower/ Gadget
    6 = Brawl Box
    7 = Tickets
    8 = Power Points (for a specific brawler)
    9 = Token Doubler
    10 = Mega Box
    11 = Keys (???)
    12 = Power Points
    13 = EventSlot (???)
    14 = Big Box
    15 = AdBox (not working anymore)
    16 = Gems

    """



    offers = [       
    
    
       {
            'ID': [16, 16, 16],
            'OfferTitle': 'возможно',
            'OfferBGR': 'offer_special',
            'ETType': 1,
            'ETMultiplier': 7,
            'Cost': 29,
            'Multiplier': [9, 6, 6],
            'OfferView': 2,
            'BrawlerID': [0, 0, 0],
            'SkinID': [0, 0, 0],
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 5184000
        },

        
        {
            'ID': 3,
            'OfferTitle': 'ОСОБАЯ АКЦИЯ',
            'Cost': 79,
            'Multiplier': 1,
            'BrawlerID': 32,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 69420,
            'Fone': "offer_generiс"
        },
                                           
        {
            'ID': 3,
            'OfferTitle': 'БРАВЛЕР',
            'Cost': 249,
            'Multiplier': 1,
            'BrawlerID': 12,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 6942,
            'Fone': "offer_generic"
        },
                      
        {
            'ID': 3,
            'OfferTitle': 'БРАВЛЕР',
            'Cost': 119,
            'Multiplier': 1,
            'BrawlerID': 11,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 6942,
            'Fone': "offer_lny"                
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 149,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 128,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival"
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 179,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 96,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival" 
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 2500,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 102,
            'ShopType': 3,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_legendary" 
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 89,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 120,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival"                        
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 79,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 173,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival"
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 99,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 126,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival"
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 0,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 52,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival"                       
        },
        
        {
            'ID': 4,
            'OfferTitle': 'СКИН',
            'Cost': 149,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 30,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'Fone': "offer_moon_festival"        
        },
        
        {
            'ID': 10,
            'OfferTitle': 'ЛАСТ ДЕНЬ',
            'Cost': 49,
            'Multiplier': 1,
            'BrawlerID': 0,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 100000,
            'TypeB': 1,
            'Banefit': 2,
            'Fone': "offer_moon_festival"              
        },
        
        {
            'ID': 3,
            'OfferTitle': 'ВОЛЬТ',
            'Cost': 299,
            'Multiplier': 1,
            'BrawlerID': 38,
            'SkinID': 0,
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 6942,
            'Fone': "offer_chromatic"                
        }
          
    ]


    gold = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        },

        {
            'Cost': 280,
            'Amount': 2600
        },

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 5
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 10
        }

    ]


    token_doubler = {

        'Cost': 40,
        'Amount': 1000
    }


      def EncodeShopOffers(self):
        count = len(Shop.offers)
        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]

            if item['ID'][0] != 0 and item['ID'][1] != 0 and item['ID'][2] != 0:
                self.writeVint(3)
                
                self.writeVint(item['ID'][0]) # ItemID
                self.writeVint(item['Multiplier'][0]) # Amount
                self.writeScId(16, item['BrawlerID'][0]) # Brawler ID
                self.writeVint(item['SkinID'][0]) # Skin ID
                
                self.writeVint(item['ID'][1]) # ItemID
                self.writeVint(item['Multiplier'][1]) # Amount
                self.writeScId(16, item['BrawlerID'][1]) # Brawler ID
                self.writeVint(item['SkinID'][1]) # Skin ID
                
                self.writeVint(item['ID'][2]) # ItemID
                self.writeVint(item['Multiplier'][2]) # Amount
                self.writeScId(16, item['BrawlerID'][2]) # Brawler ID
                self.writeVint(item['SkinID'][2]) # Skin ID

            elif item['ID'][0] != 0 and item['ID'][1] != 0:
                self.writeVint(2)
                
                self.writeVint(item['ID'][0]) # ItemID
                self.writeVint(item['Multiplier'][0]) # Amount
                self.writeScId(16, item['BrawlerID'][0]) # Brawler ID
                self.writeVint(item['SkinID'][0]) # Skin ID
                
                self.writeVint(item['ID'][1]) # ItemID
                self.writeVint(item['Multiplier'][1]) # Amount
                self.writeScId(16, item['BrawlerID'][1]) # Brawler ID
                self.writeVint(item['SkinID'][1]) # Skin ID

            else:
                self.writeVint(1)
                
                self.writeVint(item['ID'][0]) # ItemID
                self.writeVint(item['Multiplier'][0]) # Amount
                self.writeScId(16, item['BrawlerID'][0]) # Brawler ID
                self.writeVint(item['SkinID'][0]) # Skin ID

            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]
            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer']) # Timer(Seconds)

            self.writeVint(item['OfferView']) # Offer View | 0 = Absolutely "NEW", 1 = "NEW", 2 = Viewed
            self.writeVint(100)
            self.writeBoolean(False)  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0) # 'Special Offer' Text if Number > 0

            self.writeInt(0)
            self.write_string_reference(item['OfferTitle'])
            self.writeBoolean(False)
            self.writeString(item['OfferBGR']) # BGR Name
            self.writeVint(0)
            self.writeBoolean(False) # if True background disappear
            self.writeVint(item['ETType']) # Extra Text Type | 1 = Factor(?x), 2 = Percent(?%)
            self.writeVint(item['ETMultiplier']) # Extra Text
            