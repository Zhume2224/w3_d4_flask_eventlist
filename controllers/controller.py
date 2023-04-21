from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import *



@app.route('/events')
def index():
    return render_template('index.jinja', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_new_event():
    # print('ADD TASK', request.form)
    date=request.form['date']
    event_name=request.form['event_name']
    guest_number=request.form['guest_number']
    recurring = True if 'recurring' in request.form else False
    room=request.form['room']
    description=request.form['description']
    new_event=Event(date,event_name,guest_number,recurring,room,description)
    add_new_event(new_event)
    return index()

