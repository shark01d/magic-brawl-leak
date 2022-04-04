class Notifications:
    """
    << Notification IDs List >>
    
    81 = Custom Message
    82 = Club Message
    74 = Ticket Compensation Message
    
    """



    messages = [

        {
            'NotificationID': 74,
            'NotificationIndex': 3,
            'NotificationRead': True,
            'NotificationTime': 43200,
            'NotificationText': f'Компенсация за билеты',
            'Tickets': 25,
            'Gems': 300х1,
        },

        {
            'NotificationID': 81,
            'NotificationIndex': 3,
            'NotificationRead': False,
            'NotificationTime': 43200,
            'NotificationText': f'нет.',
        },

        {
            'NotificationID': 82,
            'NotificationIndex': 3,
            'NotificationRead': False,
            'NotificationTime': 43200,
            'SenderName': 'suka',
            'SenderThumbnail': 0,
            'SenderNameColor': 6,
            'NotificationText': f'.',
        },

    ]
    
    
    
    def EncodeNotificationsMessages(self):
        count = len(Notifications.messages)
        self.writeVint(count) # Count
        for i in range(count):
            item = Notifications.messages[i]
            
            self.writeVint(item['NotificationID'])
            self.writeInt(item['NotificationIndex'])
            self.writeBoolean(item['NotificationRead'])
            self.writeInt(item['NotificationTime'])
            self.writeString(item['NotificationText'])
            
            if item['NotificationID'] == 81:
                self.writeVint(0)

            elif item['NotificationID'] == 82:
                self.writeString(item['SenderName'])
                self.writeVint(100)
                self.writeVint(28000000 + item['SenderThumbnail'])
                self.writeVint(43000000 + item['SenderNameColor'])
                self.writeVint(-1)
            
            elif item['NotificationID'] == 74:
                self.writeVint(item['Tickets'])
                self.writeVint(item['Gems'])
            
            elif item['NotificationID'] == 77:
                self.writeVint(1)
                for i in range(1):
                    self.writeVint(1)
                    self.writeVint(14)  # ItemType
                    self.writeVint(1)
                    self.writeVint(0)  # CsvID
                    self.writeVint(0)
                self.writeVint(7)
                self.writeVint(3)
                self.writeString('SUMMER SPORTS CHALLENGE!')
