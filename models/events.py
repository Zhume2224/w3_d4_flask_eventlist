from models.event import *

event1 = Event("today", "Staff Meeting", 35,  True, 'EDI1', "All staff meeting")
event2 = Event("tommorow", "1-1 review", 2,  False, 'GLA3', "1-1 Review for weekend Homework")
event3 = Event("two days from now", "Quiz Night", 40,  False, 'Open Area', "Quiz night for all cohorts")
# event4=Event("next Monday", "Pajama Coding Day", 33,  False, 'Hopper Room', "wear your pjama and code comfortablly")
events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)

