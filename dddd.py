from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import json

import pickle

class ActionWeatherd(Action):
    def name(self):
        return 'action_doctord'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('doctor')







        response = json.dumps(tracker.current_slot_values())

        # if loc == 'Prof. Dr. Fikret Arpacı':
           # response = response + "loc"



        #response = "abc\n\nasd"

        dispatcher.utter_message(loc)
        #dispatcher.utter_button_message("abc", [{"abc":1}])
        return []
