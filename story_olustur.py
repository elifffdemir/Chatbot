# -*- coding: utf-8 -*-

import datetime


dep_doc = [
    {"algology" : ["Oznur Oken"]},
    {"brain and neurosurgery" : ["Gulsah Bademci", "Suat CANBAY"]},
    {"child hematology" : ["Hatice Emel Ozyurek"]},
    {"child nephrology" : ["Suleyman Kalman"]},
    {"child health and illness" : ["Musa Kazim Caglar", "Suleyman Kalman", "Hatice Emel Ozyurek", "Pakize Elif Alkıisn", "Mustafa Yucel Kiziltan", "Gokalp Basbozkurt", "Hafsa Ucur", "Husniye Altan", "Sarkhan Elbayiyev", "Shahin Guliyev"]},
    {"dermatology" : ["Aylin Gozubuyukogullari", "Yesim Akpinar Kara"]},
    {"diet policlinic" : ["Gaye Baskurt", "Deniz Ozdemir", "Halime Besler"]},
    {"endocrinology" : ["Serdar Guler"]},
    {"infectious diseases" : ["Mine Isik Arigun"]},
    {"physical therapy and rehabilitation" : ["Oznur Oken", "Beril Ozturan"]},
    {"general surgery" : ["Mehmet Mahir Ozmen", "Cem Emir Guldogan", "Emre Gundogdu"]},
    {"chest diseases" : ["Ugur Gonullu"]},
    {"eye diseases" : ["Samim Ozdes"]},
    {"hematology policlinic" : ["Oral Nevruz"]},
    {"internal diseases" : ["Beril Akman", "Sercan Cansaran", "Sevgi Karabuga", " Gokhan Celbek"]},
    {"gynecology and Obstetrics" : ["Muberra Namli Kalem", "Coskun Simsir", "Ali Ergun", "Korhan Kahraman", "Turgut Var", "Turkan Ornek Gulpınar", "Asli Yuceturk", "Ebru Yuce", "Timur Gurgan"]},
    {"cardiac surgery" : ["Erol Sener", "Emre Boysan", "Renda Circi"]},
    {"cardiology" : ["Erdogan Ilkay", "Alper Canbay", "Cigdem Koca Tari", "Erol Kalender"]},
    {"ENT diseases" : ["Ali Altuntas", "Serdar Karahatay", "Canset Aydin"]},
    {"nephrology" : ["Beril Akman"]},
    {"neurology" : ["Mehmet Zulkuf Onal", "Akcay Ovunc Ozon"]},
    {"orthopedics and traumatology" : ["Ugur Gonc", "Mesut Atabek", "levent Celebi"]},
    {"plastic surgery" : ["Ergin Isik", " Serdar Duzgun"]},
    {"psychiatry" : ["Ali Bozkurt"]},
    {"psychologist" : ["Ezgi Kilinc"]},
    {"rheumatology" : ["Orhan Kucuksahin"]},
    {"medical oncology" : ["Fikret Arpaci", "Gokhan Erdem"]},
    {"urology" : ["Musait doktor bulunmamaktadır..."]}
]
# departmanlar = ["algology", "brain and neurosurgery", "child hematology", "child nephrology",
#                 "child health and illness", "dermatology", "diet policlinic", "endocrinology",
#                 "infectious diseases", "physical therapy and rehabilitation", "gastroenterology", "general surgery",
#                 "chest diseases", "eye diseases", "hematology policlinic", "internal diseases", "gynecology and Obstetrics",
#                 "cardiac surgery", "cardiology", "ENT diseases", "nephrology", "neurology",
#                 "orthopedics and traumatology", "plastic surgery", "psychiatry", "psychologist", "rheumatology", "medical oncology",
#                 "urology"]
#
# doktorlar = ["Oznur Oken", "Gulsah Bademci", " Gulsah Bademci", "Hatice Emel Ozyurek", "Suleyman Kalman", "Musa Kazim Caglar", "Suleyman Kalman", "Hatice Emel Ozyurek", "Pakize Elif Alkis", "Mustafa Yucel Kiziltan", "Gokalp Basbozkurt", "Hafsa Ucur", "Husniye Altan", "Sarkhan Elbayiyev", "Shahin Guliyev", "Aylin Gözubuyukogullari",
#              "Yesim Akpinar Kara", "Gaye Baskurt", "Deniz Ozdemir", "Halime Besler", "Serdar Guler", "Mine Isık Arigun", "Oznur Oken", "Beril Ozturan", "Reskan Altun", "Yasemin Ozderin Ozin", "Mehmet Mahir Ozmen", "Cem Emir Guldogan", "Emre Gundogdu", "Ugur Gonullu", "Samim Ozdes", "Oral Nevruz", "Beril Akman", "Sercan Cansaran", "Sevgi Karabuga",
#              "Gokhan Celbek", "Muberra Namli Kalem", "Coskun Simsir", "Ali Ergun", "Korhan Kahraman", "Turgut Var", "Turkan Ornek Gulpinar", "Asli Yuceturk", "Ebru Yuce", "Timur Gurgan", "Erol Sener", "Emre Boysan", "Renda Circi", "Erdogan Ilkay", "Alper Canbay", "Cigdem Koca Tari", "Erol Kalender", "Ali Altuntas", "Serdar Karahatay", "Canset Aydin",
#              "Beril Akman", "Mehmet Zulkuf Onal", "Akcay Ovunc Ozon", "Ugur Gonc", "Mesut Atabek", "Levent Celebi", "Ergin Isık", "Serdar Duzgun", "Ali Bozkurt", "Ezgi Kılınc", "Orhan Kuçuksahin", "Fikret Arpaci", "Gokhan Erdem"]
sehirler = ["ankara", "istanbul", "samsun"]

gunler = {"next monday", "next tuesday", "next wednesday", "next thursday", "next friday", "next saturday", "next sunday"}
storyId = 0

file = open("stories.md", "w")
date = datetime.date.today()
for gun in gunler:
    for sehir in sehirler:
        for item in dep_doc:
            for item1 in list(item.values())[0]:
                template = """ ## Generated Story %s
                * greet
                    - utter_greet
                * appointment{"appointment": "appointment"}
                    - utter_ask_location
                * location{"location": "%s"}
                    - utter_ask_department
                * department{"department": "%s"}
                    - slot{"department": "%s"}
                    - action_doctor
                    - utter_ask_doctor
                * doctor{"doctor": "%s"} 
                    - slot{"doctor": "%s"}
                    - action_doctord 
                    - utter_ask_date 
                * date{"date": "%s"}
                    - utter_ask_tc
                * goodbye
                    - utter_goodbye\n""" % ( storyId, sehir, list(item.keys())[0], list(item.keys())[0], item1, item1,gun,)
                storyId +=1
                file.write(template)
                file.flush()

file.close()


# ad = "dcb"
# template = "senin adın {0} "
# formatli = template.format(ad)
# print(formatli)
