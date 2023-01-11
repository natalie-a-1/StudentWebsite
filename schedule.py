import datetime


class Schedule:
    def __init__(self):
        pass

    @staticmethod
    def getSchedule():
        today = datetime.datetime.today().weekday()
        schedule = {}
        if today == (0 or 6):
            schedule = {}
        elif today == (1 or 3):
            schedule = {
                ('8:00 am', '11:00 am'): 'work',
                ('11:30 am', '12:20 pm'): 'principles of programming',
                ('1:30 pm', '2:20 pm'): 'linear algebra',
                ('3:30 pm', '5:15 pm'): 'professional development',
            }
        elif today == (2 or 4):
            schedule = {
                ('9:00 am', '10:15 am'): 'intro to operating systems',
                ('11:30 am', '12:20 pm'): 'work',
                ('4:30 pm', '5:15 pm'): 'software engineering',

            }
        elif today == 5:
            schedule = {
                ('8:00 am', '11:00 am'): 'work',
                ('11:30 am', '12:20 pm'): 'principles of programming',
                ('1:30 pm', '2:20 pm'): 'linear algebra',
            }
        return schedule
