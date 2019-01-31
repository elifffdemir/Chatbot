from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button, Element, Dispatcher
import json
import pickle

randevu_yok = "Randevu almanıza gerek yoktur. Direlt acile gidebilirsiniz. Kontrol yoktur."
cm = "Randevu ÇM den verilir."
cm1 = "Randevu ÇM den verilir. Kontrol süresi 10 gündür."
cm2 = "Randevu ÇM den verilir. Kontrolü yoktur, her geliş ücrete tabidir."
durum3 = "İşlem randevuları bölüm tarafından verilir."
randevu = "Ilk randevu verilebilir."
bolum = "Bolume yonlendirilecektir."
durum4 = "Kontrol süresi 10 gündür."
asd = " "



class Info_story(Action):
    def name(self):
        return 'information'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('info')
        department = None
        buttons = None
        response = None

        # response = '#' + json.dumps(aaa) + '#'

        if loc == 'acrep socks':
            response = randevu_yok

        elif loc == 'bee sting':
            response = randevu_yok

        elif loc == 'bug bite':
            response = randevu_yok

        elif loc == 'freeze':
            response = randevu_yok

        elif loc == 'general body trauma':
            response = randevu_yok

        elif loc == 'follow-up of serum':
            response = randevu_yok

        elif loc == 'injection':
            response = randevu_yok

        elif loc == 'snaking':
            response = randevu_yok

        elif loc == 'neuropathic pain':
            response = cm1
            department = "algology"
            buttons = [
                Button(title="Prof. Dr. Oznur Oken", payload="/Dr1")
            ]

        elif loc == 'chronic pain':
            response = cm1
            department = "algology"
            buttons = [
                Button(title="Prof. Dr. Oznur Oken", payload="/Dr1")
            ]

        elif loc == 'implant':
            response = durum3 + randevu
            department = "mouth and dental health"
            buttons = [
                Button(title="There is not available doctor.", payload="/Dr1")
            ]

        elif loc == 'prosthesis':
            response = durum3 + bolum
            department = "mouth and dental health"
            buttons = [
                Button(title="There is not available doctor.", payload="/Dr1")
            ]

        elif loc == 'endodontics':
            response = durum3 + bolum
            department = "mouth and dental health"
            buttons = [
                Button(title="There is not available doctor.", payload="/Dr1")
            ]

        elif loc == 'orthodontics':
            response = durum3 + bolum
            department = "mouth and dental health"
            buttons = [
                Button(title="There is not available doctor.", payload="/Dr1")
            ]

        elif loc == 'jaw surgery':
            response = durum3 + bolum
            department = "mouth and dental health"
            buttons = [
                Button(title="There is not available doctor.", payload="/Dr1")
            ]

        elif loc == 'peridontology, implantology':
            response = durum3 + bolum
            department = "mouth and dental health"
            buttons = [
                Button(title="There is not available doctor.", payload="/Dr1")
            ]

        elif loc == 'diabetes (TIP1, TIP2) nutrition':
            response = cm2 + asd
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'obesity feeding':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'metabolic diseases, heart disease nutrition':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'obesity and diabetes nutrition':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition in metabolic syndrome':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition in heart diseases':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition in polystic over syndrome':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition for pregnant and lactating mothers':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Gaye Baskurt", payload="/Dr1")
            ]


        elif loc == 'Nutrition for children over 10':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'adolescent feeding':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition for individuals who want to gain weight':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition in oncology patients':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'constipation / gas-bloating / reflux (digestive system diseases) nutrition':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'nutrition in eating disorders':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'corporate nutrition':
            response = cm2
            department = "nutrition and diet"
            buttons = [
                Button(title="Dyt. Deniz Ozdemir", payload="/Dr1"),
                Button(title="Dyt. Gaye Baskurt", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'diagnosis and treatment services for brain and spinal cord diseases':
            response = cm1
            department = "brain and neurosurgery (neurosurgery)"
            buttons = [
                Button(title="Prof. Dr. Ethem Beskonakli", payload="/Dr1"),
                Button(title="Uzm. Dr. Cetin Akyol", payload="/Dr2"),
                Button(title="Doc. Dr. Gulsah Bademci", payload="/Dr3")
            ]

        elif loc == 'belly button':
            response = cm1
            department = "brain and neurosurgery (neurosurgery)"
            buttons = [
                Button(title="Prof. Dr. Ethem Beskonakli", payload="/Dr1"),
                Button(title="Uzm. Dr. Cetin Akyol", payload="/Dr2"),
                Button(title="Doc. Dr. Gulsah Bademci", payload="/Dr3")
            ]

        elif loc == 'neck hernia':
            response = cm1
            department = "brain and neurosurgery (neurosurgery)"
            buttons = [
                Button(title="Prof. Dr. Ethem Beskonakli", payload="/Dr1"),
                Button(title="Uzm. Dr. Cetin Akyol", payload="/Dr2"),
                Button(title="Doc. Dr. Gulsah Bademci", payload="/Dr3")
            ]

        elif loc == 'brain and spinal tumors':
            response = cm1
            department = "brain and neurosurgery (neurosurgery)"
            buttons = [
                Button(title="Prof. Dr. Ethem Beskonakli", payload="/Dr1"),
                Button(title="Uzm. Dr. Cetin Akyol", payload="/Dr2"),
                Button(title="Doc. Dr. Gulsah Bademci", payload="/Dr3")
            ]

        elif loc == 'celebral hemorrhage':
            response = cm1
            department = "brain and neurosurgery (neurosurgery)"
            buttons = [
                Button(title="Prof. Dr. Ethem Beskonakli", payload="/Dr1"),
                Button(title="Uzm. Dr. Cetin Akyol", payload="/Dr2"),
                Button(title="Doc. Dr. Gulsah Bademci", payload="/Dr3")
            ]

        elif loc == 'complaints about brain vessels':
            response = cm1
            department = "brain and neurosurgery (neurosurgery)"
            buttons = [
                Button(title="Prof. Dr. Ethem Beskonakli", payload="/Dr1"),
                Button(title="Uzm. Dr. Cetin Akyol", payload="/Dr2"),
                Button(title="Doc. Dr. Gulsah Bademci", payload="/Dr3")
            ]

        elif loc == 'checkup':
            response = cm1
            department = "checkup"
            buttons = [
                Button(title="Uzm. Dr. Sevgi Karabuga", payload="/Dr1"),
                Button(title="Uzm. Dr. Sercan Cansaran", payload="/Dr2")
            ]

        elif loc == 'allianz insurance family medicine':
            response = cm
            department = "checkup"
            buttons = [
                Button(title="Doc. Dr. Reskan Altun", payload="/Dr1"),
                Button(title="Doc. Dr. Beril Akman", payload="/Dr2")
            ]

        elif loc == '(0-17 years), from birth to adulthood until adulthood, is the department that applies diagnosis and treatment methods of surgical diseases that are related to congenital and / or acquired respiratory, digestive and excretory systems':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'circumcision':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'gobek fitigi':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'inguinal hernia':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'innervated testis':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'newborn surgical diseases':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            question = "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'laparoscopic interventions in children':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'pediatric thoracic surgeon':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'childhood urology':
            response = cm1 + "\n" + "Cocuk sagligi ve hastaliklari olarak da kabulunuz yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'child health and illness':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'fabry':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'juvenil idiyopatik atrit':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'mumps':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'constipation':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'measles':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'rubella':
            response = cm1 + "\n" + "Diger hekimlere de yonlendırme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'red':
            response = cm1 + "\n" + "Diger hekimlere de yonlendirme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'diphtheria':
            response = cm1 + "\n" + "Diger hekimlere de yonlendirme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'neurofibromatosis':
            response = cm1 + "\n" + "Diger hekimlere de yonlendirme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'rickets':
            response = cm1 + "\n" + "Diger hekimlere de yonlendirme yapilabilir. Istiyor musunuz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'growth and development of the baby (social / mental / speech and movement)':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'development of risky babies':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'safe toys and games suitable for development':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'adjustment of eating / sleeping regimen and toilet habit in children':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'arrangement of relations between siblings':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'behavioral disorders (lowering, nail-eating, finger sucking, irritability, stubbornness, etc.)':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'to determine the best age for starting a child\'s nursery or primary school':
            response = durum4 + "\n" + "Uygun doktor bulunmamaktadır."
            department = "child development"

        elif loc == 'child blood diseases, anemia':
            response = cm1 + "\n" + "16 yasindan buyuk cocuklar icin yetiskin hematolojiye randevu verilebilir. Ister misiniz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'childhood cancers':
            response = cm1 + "\n" + "16 yasindan buyuk cocuklar icin yetiskin hematolojiye randevu verilebilir. Ister misiniz?"
            buttons = [
                Button(title="yes", payload="/Dr1"),
                Button(title="no", payload="/Dr2")
            ]

        elif loc == 'congenital heart diseases':
            response = durum4

        elif loc == 'adolescent and adult age-related heart diseases':
            response = durum4

        elif loc == 'rheumatic heart diseases':
            response = durum4

        elif loc == 'interventional treatment of pediatric cardiology (transcatheter closure of congenital heart defects, balloon valvuloplasty and angioplasty)':
            response = durum4

        elif loc == 'None':
            response = durum4

        elif loc == 'None':
            response = durum4

        elif loc == 'child-adolescent psychodynamic-oriented psychotherapy':
            response = cm2

        elif loc == 'group therapy':
            response = cm2

        elif loc == 'psychodrama':
            response = cm2

        elif loc == 'lack of attention':
            response = cm2

        elif loc == 'hyperactivity':
            response = cm2

        elif loc == 'childhood traumas':
            response = cm2

        elif loc == 'asthma and allergy diseases':
            response = cm2

        elif loc == 'asthma':
            response = cm2

        elif loc == 'whistling children':
            response = cm2

        elif loc == 'allergic rhinitis':
            response = cm2

        elif loc == 'eye allergy':
            response = cm2

        elif loc == 'urticaria':
            response = cm2

        elif loc == 'eczema (atopic dermatitis)':
            response = cm2

        elif loc == 'drug allergies':
            response = cm2

        elif loc == 'bee allergy':
            response = cm2

        elif loc == 'hereditary angioedema':
            response = cm1

        elif loc == 'food allergies (cow|\'s milk allergy and other food allergies)':
            response = cm1

        elif loc == 'diseases of immunology':
            response = cm1

        elif loc == 'immunodeficiencies (immunodeficiency)':
            response = cm1

        elif loc == 'infected children':
            response = cm1

        elif loc == 'respiratory tract diseases':
            response = cm1

        elif loc == 'recurrent lung infections':
            response = cm1

        elif loc == 'cystic fibrosis':
            response = cm

        elif loc == 'bronchiectasis':
            response = cm1

        elif loc == 'chronic lung diseases':
            response = cm1

        elif loc == 'sleep apnea problems':
            response = cm1

        elif loc == 'skin prick test (allergy tests)':
            response = cm1

        elif loc == 'patch test (skin patch test)':
            response = cm1

        elif loc == 'pulmonary function tests':
            response = cm1

        elif loc == 'drug allergy tests':
            response = cm1

        elif loc == 'nitrate nitric oxide measurement':
            response = cm1

        elif loc == 'sweat test':
            response = cm1

        elif loc == 'Pediatric Kidney Diseases / Urinary tract problems / Urinary incontinence problems / Mediterranean fever / Kidney stones in children (urology if surgery is needed) / Protein leaking / Night abduction / Hypertension':
            response = cm1

        elif loc == 'Rheumatoid arthritis / vasculitis vasculitis':
            response = cm1

        elif loc == 'a major part of the adult patient group is the main chapter on the diagnosis and resolution of internal health problems':
            response = cm1

        elif loc == 'high fever':
            response = cm1

        elif loc == 'weakness':
            response = cm1

        elif loc == 'abdominal pain':
            response = cm1

        elif loc == 'diarrhea':
            response = cm1

        elif loc == 'high cholesterol':
            response = cm1

        elif loc == 'bruising without any reason in the body':
            response = cm1

        elif loc == 'flu':
            response = cm1

        elif loc == 'hypertension':
            response = cm1

        elif loc == 'sweating':
            response = cm

        elif loc == 'nausea':
            response = cm

        elif loc == 'evaluation of blood results':
            response = cm


        if response is not None:
            dispatcher.utter_message(response)
        if buttons is not None:
            dispatcher.utter_button_message(" ", buttons)

        retval = []
        if loc is not None:
            retval.append(SlotSet('info', loc))
        if department is not None:
            retval.append(SlotSet('department', department))
        return retval
