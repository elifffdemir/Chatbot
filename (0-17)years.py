from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button, Element, Dispatcher
import json
import pickle



class Answer_Info(Action):
    def name(self):
        return 'answer_info'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('answer')
        department = tracker.get_slot('department')
        # question = "Hangi departmandan randevu almak istersiniz?"
        # response = tracker.current_slot_values()
        buttons = []

        if loc == 'nope':
            department = "child surgeon"
            buttons = [
                Button(title="Doc. Dr. Mustafa Kemal Aslan", payload="/btn1")
            ]
        elif loc == 'yes':
            department = "child health and illness"
            buttons = [
                Button(title="Prof. Dr. Musa Kazim Caglar", payload="/btn1"),
                Button(title="Prof. Dr. Suleyman Kalman", payload="/btn2"),
                Button(title="Prof. Dr. Hatice Emel Ozyurek", payload="/btn3"),
                Button(title="Yar. Doc. Dr. Pakize Elif Alkisn", payload="/btn4"),
                Button(title="Uzm. Dr. Mustafa Yucel Kiziltan", payload="/btn5"),
                Button(title="Uzm. Dr. Gokalp Basbozkurt", payload="/btn6"),
                Button(title="Uzm. Dr. Hafsa Ucur", payload="/btn7"),
                Button(title="Uzm. Dr. Husniye Altan", payload="/btn8"),
                Button(title="Uzm. Dr. Sarkhan Elbayiyev", payload="/btn9"),
                Button(title="Uzm. Dr. Shahin Guliyev", payload="/btn10")
            ]
    
        # dispatcher.utter_message(response)
        dispatcher.utter_button_message(" ", buttons)

        retval = []
        if department is not None:
            retval.append(SlotSet('department', department))
        if loc is not None:
            retval.append(SlotSet('answer', loc))

        return retval


