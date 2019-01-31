from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button, Element, Dispatcher
import json
import pickle

class ActionWeather(Action):
    def name(self):
        return 'action_doctor'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('department')

        if loc == 'algology':
            buttons = [
                Button(title="Prof. Dr. Oznur Oken", payload="/Dr1")
            ]

        elif loc == 'brain and neurosurgery':
            buttons = [
                Button(title="Doc. Dr. Gulsah Bademci", payload="/btn1"),
                Button(title="Doc. Dr. Suat CANBAY", payload="/btn2")
            ]

        elif loc == 'child hematology':
            buttons = [
                Button(title="Prof. Dr. Hatice Emel Ozyurek", payload="/btn1")
            ]

        elif loc == 'child nephrology':
            buttons = [
                Button(title="Prof. Dr. Suleyman Kalman", payload="/btn1")
            ]

        elif loc == 'child health and illness':
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
        elif loc == 'dermatology':
            buttons = [
                Button(title="Uzm. Dr. Aylin Gozubuyukogullari", payload="/Dr1"),
                Button(title="Uzm. Dr. Yesim Akpinar Kara", payload="/Dr2")
            ]
        elif loc == 'diet policlinic':
            buttons = [
                Button(title="Uzm. Dyt. Gaye Baskurt", payload="/Dr1"),
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'endocrinology':
            buttons = [
                Button(title="Prof. Dr. Serdar Guler", payload="/Dr1")
            ]

        elif loc == 'infectious diseases':
            buttons = [
                Button(title="Uzm. Dr. Mine Isik Arigun", payload="/Dr1")
            ]

        elif loc == 'physical therapy and rehabilitation':
            buttons = [
                Button(title="Prof. Dr. Oznur Oken", payload="/Dr1"),
                Button(title="Uzm. Dr. Beril Ozturan", payload="/Dr2")
            ]

        elif loc == 'gastroenterology':
            buttons = [
                Button(title="Doc. Dr. Reskan Altun", payload="/Dr1"),
                Button(title="Doc. Dr. Yasemin Ozderin Ozin", payload="/Dr2")
            ]

        elif loc == 'general surgery':
            buttons = [
                Button(title="Prof. Dr. Mehmet Mahir Ozmen", payload="/Dr1"),
                Button(title="Yar. Doc. Dr. Cem Emir Guldogan", payload="/Dr2"),
                Button(title="Yar. Doc. Dr. Emre Gundogdu", payload="/Dr3")
            ]

        elif loc == 'chest diseases':
            buttons = [
                Button(title="Prof. Dr. Ugur Gonullu", payload="/Dr1")
            ]


        elif loc == 'eye diseases':
            buttons = [
                Button(title="Op. Dr. Samim Ozdes", payload="/Dr1")
            ]

        elif loc == 'hematology policlinic':
            buttons = [
                Button(title="Prof. Dr. Oral Nevruz", payload="/Dr1")
            ]

        elif loc == 'internal diseases':
            buttons = [
                Button(title="Doc. Dr. Beril Akman", payload="/Dr1"),
                Button(title="Uzm. Dr. Sercan Cansaran", payload="/Dr2"),
                Button(title="Uzm. Dr. Sevgi Karabuga", payload="/Dr3"),
                Button(title="Yar. Doc. Dr. Gokhan Celbek", payload="/Dr4")
            ]

        elif loc == 'gynecology and Obstetrics':
            buttons = [
                Button(title="Yar. Doc. Dr. Muberra Namli Kalem", payload="/Dr1"),
                Button(title="Yar. Doc. Dr. Coskun Simsir", payload="/Dr2"),
                Button(title="Prof. Dr. Ali Ergun", payload="/Dr3"),
                Button(title="Doc. Dr. Korhan Kahraman", payload="/Dr4"),
                Button(title="Doc. Dr. Turgut Var", payload="/Dr5"),
                Button(title="Doc. Dr. Turkan Ornek Gulpinar", payload="/Dr6"),
                Button(title="Op. Dr. Asli Yuceturk", payload="/Dr7"),
                Button(title="Op. Dr. Ebru Yuce", payload="/Dr8"),
                Button(title="Prof. Dr. Timur Gurgan", payload="/Dr9")
            ]

        elif loc == 'cardiac surgery':
            buttons = [
                Button(title="Prof. Dr. Erol Sener", payload="/Dr1"),
                Button(title="Yar. Doc. Dr. Emre Boysan", payload="/Dr2"),
                Button(title="Yar. Doc. Renda Circi", payload="/Dr3")
            ]

        elif loc == 'cardiology':
            buttons = [
                Button(title="Prof. Dr. Erdogan Ilkay", payload="/Dr1"),
                Button(title="Doc. Dr. Alper Canbay", payload="/Dr2"),
                Button(title="Uzm. Dr. Cigdem Koca Tari", payload="/Dr3"),
                Button(title="Uzm. Dr. Erol Kalender", payload="/Dr4")
            ]

        elif loc == 'ENT diseases':
            buttons = [
                Button(title="Prof. Dr. Ali Altuntas", payload="/Dr1"),
                Button(title="Prof. Dr. Serdar Karahatay", payload="/Dr2"),
                Button(title="Yar. Doc. Dr. Canset Aydin", payload="/Dr3")
            ]

        elif loc == 'nephrology':
            buttons = [
                Button(title="Doc. Dr. Beril Akman", payload="/Dr1")
            ]

        elif loc == 'neurology':
            buttons = [
                Button(title="Prof. Dr. Mehmet Zulkuf Onal", payload="/Dr1"),
                Button(title="Yar. Doc. Dr. Akcay Ovunc Ozon", payload="/Dr2")
            ]

        elif loc == 'orthopedics and traumatology':
            buttons = [
                Button(title="Yar. Doc. Dr. Ugur Gonc", payload="/Dr1"),
                Button(title="Op. Dr. Mesut Atabek", payload="/Dr2"),
                Button(title="Prof. Dr. levent Celebi", payload="/Dr3")

            ]

        elif loc == 'plastic surgery':
            buttons = [
                Button(title="Op. Dr. Ergin Isik", payload="/Dr1"),
                Button(title="Op. Dr. Serdar Duzgun", payload="/Dr2")

            ]

        elif loc == 'psychiatry':
            buttons = [
                Button(title="Prof. Dr. Ali Bozkurt", payload="/Dr1")

            ]

        elif loc == 'psychologist':
            buttons = [
                Button(title="Psk. Ezgi Kılınc", payload="/Dr1")

            ]

        elif loc == 'rheumatology':
            buttons = [
                Button(title="Doc. Dr. Orhan Kucuksahin", payload="/Dr1")

            ]


        elif loc == 'medical oncology':
            buttons = [
                Button(title="Prof. Dr. Fikret Arpaci", payload="/Dr1"),
                Button(title="Doc. Dr. Gokhan Erdem", payload="/Dr2")

            ]

        elif loc == 'urology':
            buttons = [
                Button(title="Musait doktor bulunmamaktadir...", payload="/Dr1")

            ]


        dispatcher.utter_button_message("Doctors", buttons)

        response = loc

        return [SlotSet('doctor', response)]
