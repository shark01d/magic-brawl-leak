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
            'TypeB': 0,
            'Banefit': 0,
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

            self.writeVint(1)

            self.writeVint(item['ID']) # ItemID
            self.writeVint(item['Multiplier']) # Ammount
            self.writeScId(16, item['BrawlerID'])
            self.writeVint(item['SkinID'])
            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer']) # Timer

            self.writeVint(1)
            self.writeVint(100)
            self.writeBoolean(False)  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)
            
            self.writeInt(0)
            self.write_string_reference(item['OfferTitle'])
            self.writeBoolean(False)
            self.writeString(item['Fone'])
            self.writeVint(0)
            self.writeBoolean(False)
            self.writeVint(item['TypeB'])
            self.writeVint(item['Banefit']) # % Extra Text
            