from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button, Element, Dispatcher

class Child_Health(Action):
    def name(self):
        return 'child'

    def run(self, dispatcher, tracker, domain):

        department = None
        question = None
        buttons = None
        response = None
        loc = tracker.get_slot('answer')


        if loc == 'nope':
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
        else:
            question = "Diger hekimler hakkinda bilgi alabilmek icin musteri temsilcimiz ile gorusunuz."



        if response is not None:
            dispatcher.utter_message(response)
        if question is not None:
            dispatcher.utter_message(question)

        if buttons is not None:
            dispatcher.utter_button_message(" ", buttons)

        retval = list()
        if department is not None:
            retval.append(SlotSet('department', department))
        if loc is not None:
            retval.append(SlotSet('answer', loc))

        return retval


