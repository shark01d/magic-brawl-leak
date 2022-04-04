import time

class EventSlots:
    '''
    << Modifiers List >>
    1 = Energy Drink
    2 = Angry Robo
    3 = Meteor Shower
    4 = Graveyard Shift
    5 = Healing Mushrooms
    8 = Boss Lasers
    9 = Boss Chain Lighting
    10 = Boss Rockets
    11 = Ship Tilting
    
    Status | 3 = Nothing, 2 = Star Token, 1 = New Event
    '''
    Timer = 86399

    maps = [
    
        {
            'ID': 7,
            'Status': 2,
            'Ended': False,
            'Modifier': 3,
            'Tokens': 10
        },

        {
            'ID': 32,
            'Status': 2,
            'Ended': False,
            'Modifier': 5,
            'Tokens': 10
        },

        {
            'ID': 17,
            'Status': 2,
            'Ended': False,
            'Modifier': 3,
            'Tokens': 10
        },

        {
            'ID': 201,
            'Status': 2,
            'Ended': False,
            'Modifier': 4,
            'Tokens': 10
        },

        {
            'ID': 38,
            'Status': 2,
            'Ended': False,
            'Modifier': 2,
            'Tokens': 10
        },

        {
            'ID': 24,
            'Status': 2,
            'Ended': False,
            'Modifier': 5,
            'Tokens': 10
        },

        {
            'ID': 21,
            'Status': 2,
            'Ended': True,
            'Modifier': 0,
            'Tokens': 2
        },

        {
            'ID': 97,
            'Status': 2,
            'Ended': False,
            'Modifier': 11,
            'Tokens': 10
        },
        
        {
            'ID': 25,
            'Status': 2,
            'Ended': True,
            'Modifier': 0,
            'Tokens': 10
        },
        
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        {
            'ID': 56,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },
        
        {
            'ID': 23,
            'Status': 2,
            'Ended': True,
            'Modifier': 0,
            'Tokens': 10
        },
        
        {
            'ID': 180,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 50
        },

        {
            'ID': 167,
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens':10
        }
       

    ]