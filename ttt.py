from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button, Element, Dispatcher
import json
import pickle

class ActionWeathert(Action):
    def name(self):
        return 'action_doctort'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('tc')
        slot_values = tracker.current_slot_values()
        # response = '#' + json.dumps(aaa) + '#'


        #response = "abc\n\nasd"

        #response = loc
        # buttons = [
        #     Button(title="Btn1", payload="/btn1"),
        #     Button(title="Btn2", payload="/btn2")
        # ]
        response = "Veri alındı"
        dispatcher.utter_message(response)
        return []
