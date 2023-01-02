from flask import Flask, render_template
import datetime


class Schedule:
    def __init__(self):
        pass

    schedule = {}
    @staticmethod
    def getSchedule():
        today = datetime.datetime.today().weekday()
        if today == (0 or 6):
            schedule = {}
        elif today == (1 or 3):
            schedule = {
                '8:00am-11:00am': 'work',
                '11:30am-12:20pm': 'principles of programming',
                '1:30pm-2:20pm': 'linear algebra',
                '3:30pm-5:15pm': 'professional development',
            }
        elif today == (2 or 4):
            schedule = {
                '9:00am-10:15am': 'intro to operating systems',
                '11:30am-12:20pm': 'work',
                '4:30pm-5:15pm': 'software engineering',

            }
        elif today == 5:
            schedule = {
                '8:00am-11:00am': 'work',
                '11:30am-12:20pm': 'principles of programming',
                '1:30pm-2:20pm': 'linear algebra',
            }
        return schedule
