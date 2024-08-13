import os
import json

# Wechsel in der aktuellen Pfad der Datei

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
os.chdir(script_dir)

#%% Erstellung der Klasse Register_ID

class Register_ID:
    ids = []
    first_names = []
    last_names = []
    ages = []
    emails = []
    streets = []
    house_numbers = []
    post_codes = []
    citys = []
    json_pack = {}

    def __init__(self, id: int, vorname: str, nachname:str, alter: int, email: str, strasse: str, hausnummer: str, plz: int, stadt: str, **optionals) -> None:
        self.id = id
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.email = email
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.stadt = stadt
        self.optionals = optionals
        self.add_id(id, vorname, nachname, alter, email, strasse, hausnummer, plz, stadt)
        if print_register_bestaetigung == 'ja':
            self.bestaetigung_neuer_eintrag()
        else:
            pass
        self.add_json()

    def add_id(self, id: int, vorname: str, nachname:str, alter: int, email: str, strasse: str, hausnummer: str, plz: int, stadt: str):
        Register_ID.ids.append(id)
        Register_ID.first_names.append(vorname)
        Register_ID.last_names.append(nachname)
        Register_ID.ages.append(alter)
        Register_ID.emails.append(email)
        Register_ID.streets.append(strasse)
        Register_ID.house_numbers.append(hausnummer)
        Register_ID.post_codes.append(plz)
        Register_ID.citys.append(stadt)

    
    def bestaetigung_neuer_eintrag(self):
        print('\n### Neuer Datensatz wird verarbeitet ###\n')
        print(f'ID: {self.id}')
        print(f'Vorname: {self.vorname}')
        print(f'Nachname: {self.nachname}')
        print(f'Alter: {self.alter}')
        print(f'Email: {self.email}')
        print(f'Strasse: {self.strasse} {self.hausnummer}')
        print(f'PLZ / Ort: {self.plz} {self.stadt}') 
        if self.optionals:
            for key, value in self.optionals.items():
                print(f'{key}: {value}')   
        print('\n### Neuer Datensatz erfolgreich erstellt ###\n')
        
    def add_json(self):
        json_eintrag = {
            "vorname": self.vorname,
            "nachname": self.nachname,
            "alter": self.alter,
            "email": self.email,
            "strasse": self.strasse,
            'hausnummer': self.hausnummer,
            "plz": self.plz,
            "stadt": self.stadt,
            "optional": self.optionals
        }
        Register_ID.json_pack[self.id] = json_eintrag

    @classmethod
    def remove_id(cls, id: int):
        if id in cls.ids:
            index = cls.ids.index(id)
            cls.ids.pop(index)
            cls.first_names.pop(index)
            cls.last_names.pop(index)
            cls.ages.pop(index)
            cls.emails.pop(index)
            cls.streets.pop(index)
            cls.house_numbers.pop(index)
            cls.post_codes.pop(index)
            cls.citys.pop(index)
            cls.json_pack.pop(id, None)
            print('Eintrag wurde gelöscht !\n')

#%% Erstellung der Funktion einer neuen ID mit automatischer Ermittlung einzigartiger ID

def abfrage_neue_id(id_vorname: str, id_nachname: str, id_age: int, id_email: str, id_strasse: str, id_hausnummer: str, id_plz: int, id_stadt: str, **optionals) -> None:
    id = 1
    while id in Register_ID.ids:
        id += 1
    Register_ID(id, id_vorname, id_nachname, id_age, id_email, id_strasse, id_hausnummer, id_plz, id_stadt, **optionals)

#%% Erstellung der Funktion zur Input-Abfrage der neuen ID inklusive erstellung dieser ID

def eintrag_erstellen() -> None:
    id_vorname = input('Eingabe Vorname: ').capitalize()
    id_nachname = input('Eingabe Nachname: ').capitalize()
    while True:
        try:
            id_age = int(input('Eingabe Alter: '))
        except:
            print('Bitte nur Zahlen eingeben im Alter !')
        else: 
            break
    id_email = input('Eingabe E-Mail Adresse: ')
    id_strasse = input('Eingabe Straße ( ohne Hausnummer ) : ').capitalize()
    id_hausnummer = input('Eingabe Hausnummer: ')
    while True:
        try:
            id_plz = int(input('Eingabe Postleitzahl: '))
        except:
            ('Bitte nur Zahlen eingeben in der Postleitzahl !')
        else: 
            break
    id_stadt = input('Eingabe Stadt: ').capitalize()
    optionals = abfrage_optionals()
    abfrage_neue_id(id_vorname, id_nachname, id_age, id_email, id_strasse, id_hausnummer,  id_plz, id_stadt, **optionals)
    
def abfrage_optionals():
    optionals = {}
    eingabe_optionals1 = input('\nOptionale Eingaben erwünscht? (ja / nein): ').lower()
    if eingabe_optionals1 == 'ja':
        eingabe_optionals2 = int(input('Wie viele optoinale Eingaben sind gewünscht?: '))
        print()
        counter = eingabe_optionals2
        while counter > 0:
            key = input('Eingabe Key ( z.B. Hobbies, Haustiere, etc. ): ').capitalize()
            value = input('Eingabe Value: ( z.B. Tischtennis, Hunde und Katzen, etc ): ').capitalize()
            print()
            optionals[key] = value
            counter -= 1
    else:
        pass
    return optionals


#%% Erstellung der Funktion zu Detail-Abfragen 

def id_abfrage(suche: int) -> None:    
    index = Register_ID.ids.index(suche)
    print(f'ID: {Register_ID.ids[index]}')
    print(f'Vorname: {Register_ID.first_names[index]}')
    print(f'Nachname: {Register_ID.last_names[index]}')
    print(f'Alter: {Register_ID.ages[index]}')
    print(f'Email: {Register_ID.emails[index]}')
    print(f'Straße: {Register_ID.streets[index]} {Register_ID.house_numbers[index]}')
    print(f'PLZ / Ort: {Register_ID.post_codes[index]} {Register_ID.citys[index]}')
    person = Register_ID.json_pack.get(suche)
    if person:
        if person['optional']:
            print(f'\nOptionale Felder für {person['vorname']} {person['nachname']}:\n')
            for opt_key, opt_value in person['optional'].items():
                print(f'{opt_key}: {opt_value}')
        else:
            print(f"\nKeine optionalen Felder für {person['vorname']} {person['nachname']}.")

def vorname_abfrage(suche: str) -> None:
    index = [i for i, value in enumerate(Register_ID.first_names) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def nachname_abfrage(suche: str) -> None:
    index = [i for i, value in enumerate(Register_ID.last_names) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def alter_abfrage(suche: int) -> None:
    index = [i for i, value in enumerate(Register_ID.ages) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def email_abfrage(suche: str) -> None:
    index = [i for i, value in enumerate(Register_ID.emails) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def strasse_abfrage(suche: str) -> None:
    index = [i for i, value in enumerate(Register_ID.streets) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def hausnummer_abfrage(suche: str) -> None:
    index = [i for i, value in enumerate(Register_ID.house_numbers) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def plz_abfrage(suche: int) -> None:
    index = [i for i, value in enumerate(Register_ID.post_codes) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
    
def stadt_abfrage(suche: str) -> None:
    index = [i for i, value in enumerate(Register_ID.citys) if value == suche]
    for i in index:
        print(f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}')
   
#%% Erstellung der Funktionen zur Bearbeitung von Einträgen

def vorname_bearbeiten(suche):
    global datenbank_txt_name
    if suche in Register_ID.ids:
        index = Register_ID.ids.index(suche)
        vorname = input('Bitte neuen Vornamen eingeben: ')
        Register_ID.first_names[index] = vorname
        Register_ID.json_pack[suche]['vorname'] = vorname
        with open(datenbank_txt_name, 'w') as writer:
            json.dump(Register_ID.json_pack, writer)
        print('Eintrag erfolgreich bearbeitet !\n')
    
def nachname_bearbeiten(suche):
    global datenbank_txt_name
    if suche in Register_ID.ids:
        index = Register_ID.ids.index(suche)
        nachname = input('Bitte neuen Nachnamen eingeben: ')
        Register_ID.last_names[index] = nachname
        Register_ID.json_pack[suche]['nachname'] = nachname
        with open(datenbank_txt_name, 'w') as writer:
            json.dump(Register_ID.json_pack, writer)
        print('Eintrag erfolgreich bearbeitet !\n')
    

def alter_bearbeiten(suche):
    global datenbank_txt_name
    if suche in Register_ID.ids:
        index = Register_ID.ids.index(suche)
        alter = input('Bitte neues Alter eingeben: ')
        Register_ID.ages[index] = alter
        Register_ID.json_pack[suche]['alter'] = alter
        with open(datenbank_txt_name, 'w') as writer:
            json.dump(Register_ID.json_pack, writer)
        print('Eintrag erfolgreich bearbeitet !\n')
    
def email_bearbeiten(suche):
    global datenbank_txt_name
    if suche in Register_ID.ids:
        index = Register_ID.ids.index(suche)
        email = input('Bitte neue Email eingeben: ')
        Register_ID.emails[index] = email
        Register_ID.json_pack[suche]['email'] = email
        with open(datenbank_txt_name, 'w') as writer:
            json.dump(Register_ID.json_pack, writer)
        print('Eintrag erfolgreich bearbeitet !\n')
  
def adresse_bearbeiten(suche):
    global datenbank_txt_name
    if suche in Register_ID.ids:
        index = Register_ID.ids.index(suche)
        strasse = input('Bitte neue Straße eingeben ( ohne Hausnummer ): ').capitalize()
        hausnummer = input('Bitte neue Hausnummer eingeben: ')
        while True:
            try:
                postleitzahl = int(input('Bitte neue Postleitzahl eingeben: '))
            except:
                print('Bitte nur Zahlen eingeben !')
            else:
                break
        stadt = input('Bitte neue Stadt eingeben: ').capitalize()
        Register_ID.streets[index] = strasse
        Register_ID.house_numbers[index] = hausnummer
        Register_ID.post_codes[index] = postleitzahl
        Register_ID.citys[index] = stadt
        Register_ID.json_pack[suche]['strasse'] = strasse
        Register_ID.json_pack[suche]['hausnummer'] = hausnummer
        Register_ID.json_pack[suche]['plz'] = postleitzahl
        Register_ID.json_pack[suche]['stadt'] = stadt
        with open(datenbank_txt_name, 'w') as writer:
            json.dump(Register_ID.json_pack, writer)
        print('Eintrag erfolgreich bearbeitet !\n')
  
#%% Ladern der Datenbank

datenbank_txt_name = 'Datenbank_Register_ID.txt'
print_register_bestaetigung = 'nein'
try:
    with open(datenbank_txt_name) as reader:
        json_pack = json.load(reader)    
    print('##### Intialisierung Datenbank #####\n')
    print('Datenbank gefunden, wird geladen...\n')
    for i in json_pack:
            vorname = json_pack[i].get('vorname')
            nachname = json_pack[i].get('nachname')
            alter = json_pack[i].get('alter')
            email = json_pack[i].get('email')
            strasse = json_pack[i].get('strasse')
            hausnummer = json_pack[i].get('hausnummer')
            plz = json_pack[i].get('plz')
            stadt = json_pack[i].get('stadt')
            optional = json_pack[i].get('optional', {})
            erstelle_eintrag = Register_ID(int(i),vorname, nachname, alter, email, strasse, hausnummer, plz, stadt, **optional)  
    print_register_bestaetigung = 'ja'  
    print('##### Initialisierung beendet - Einträge geladen #####\n')

except:
    print('##### Intialisierung Datenbank #####\n')
    print('Es ist keine aktuelle Datenbank vorhanden. Neue Datenbank erstellt !\n')
    print('##### Intialisierung beendet #####\n')
    with open('Datenbank_Register_ID.txt', 'w') as writer:
        writer.write('')
    print_register_bestaetigung = 'ja'
    
#%% Hauptmenü

while True:
    print('-- Hauptmenü --\n')
    print('( 1 ) Datensätzen durchsuchen')
    print('( 2 ) Neuen Eintrag erstellen')
    print('( 3 ) Einträge bearbeiten')
    print('( 4 ) Datensatz löschen\n')
    print('( 5 ) Programm beenden')
    while True:
        try:
            eingabe_hauptmenue = int(input('\nEingabe: '))
        except:
            print('Bitte nur Zahlen eingeben !')
        else: 
            break

#%% Datensätze durchsuchen

    if eingabe_hauptmenue == 1:
        while True:
            print('\n-- Datensätze durchsuchen: --\n')
            print('( 1 )  Datensätze anzeigen   ( einfach  -> ohne optionale Einträge )')            
            print('( 2 )  ID - Abfrage          ( komplett -> mit  optionale Einträge )\n')
            print('( 3 )  Suche nach: Vorname')
            print('( 4 )  Suche nach: Nachname')
            print('( 5 )  Suche nach: Alter')
            print('( 6 )  Suche nach: Email')
            print('( 7 )  Suche nach: Straße')
            print('( 8 )  Suche nach: Hausnummer')
            print('( 9 )  Suche nach: Postleitzahl')
            print('( 10 ) Suche nach: Stadt\n')
            print('( 11 ) Zurück zum Hauptmenü')
            while True:
                try:
                    eingabe_datensaetze_durchsuchen = int(input('\nEingabe: '))
                except:
                    print('Bitte nur Zahlen eingeben !')
                else: 
                    break
            if eingabe_datensaetze_durchsuchen == 1:
                print('\n### Datensätze werden geladen ###\n')
                for index, value in enumerate(Register_ID.ids):
                    print(f'ID: {Register_ID.ids[index]} - {Register_ID.first_names[index]} {Register_ID.last_names[index]}, {Register_ID.ages[index]} Jahre alt, {Register_ID.emails[index]}, {Register_ID.streets[index]} {Register_ID.house_numbers[index]}, {Register_ID.post_codes[index]} {Register_ID.citys[index]}')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 2:
                suchen = int(input('Bitte ID eingeben: '))
                print('\n### Datensätze werden geladen ###\n')
                try:
                    id_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit der ID: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 3:
                suchen = input('Bitte Vorname eingeben: ').capitalize()
                print('\n### Datensätze werden geladen ###\n')
                try:
                    vorname_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit dem Vornamen: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 4:
                suchen = input('Bitte Nachname eingeben: ').capitalize()
                print('\n### Datensätze werden geladen ###\n')
                try:
                    nachname_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit dem Nachnamen: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 5:
                suchen = int(input('Bitte Alter eingeben: '))
                print('\n### Datensätze werden geladen ###\n')
                try:
                    alter_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit dem Alter: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 6:
                suchen = input('Bitte Email eingeben: ')
                print('\n### Datensätze werden geladen ###\n')
                try:
                    email_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit der Email: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 7:
                suchen = input('Bitte Straße eingeben: ').capitalize()
                print('\n### Datensätze werden geladen ###\n')
                try:
                    strasse_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit dem Straßennamen: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 8:
                suchen = input('Bitte Hausnummer eingeben: ')
                print('\n### Datensätze werden geladen ###\n')
                try:
                    hausnummer_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit der Hausnummer: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')    
            elif eingabe_datensaetze_durchsuchen == 9:
                suchen = int(input('Bitte Postleitzahl eingeben: '))
                print('\n### Datensätze werden geladen ###\n')
                try:
                    plz_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit der Postleitzahl: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 10:
                suchen = input('Bitte Stadt eingeben: ').capitalize()
                print('\n### Datensätze werden geladen ###\n')
                try:
                    stadt_abfrage(suchen)
                except:
                    print(f'Keine Einträge mit der Stadt: {suchen} gefunden !')
                print('\n### Datensätze vollständig geladen ###\n')
                input('- Weiter mit belibiger Taste -')
            elif eingabe_datensaetze_durchsuchen == 11:
                print()
                break

#%% Neuen Eintrag erstellen

    elif eingabe_hauptmenue == 2:
        eintrag_erstellen()
        
        with open(datenbank_txt_name, 'w') as writer:
            json.dump(Register_ID.json_pack, writer)       

#%% Einträge bearbeiten

    elif eingabe_hauptmenue == 3:
        while True:
            print('\n-- Einträge bearbeiten: --\n')
            try:
                eingabe_eintraege_bearbeiten1 = int(input('Bitte zu bearbeitende ID eingeben: '))
            except  ValueError:
                print('Eingabe abgebrochen\n')
                break
            except:
                print(f'ID {eingabe_eintraege_bearbeiten1} nicht gefunden !')
                break
            else:
                print()
                id_abfrage(eingabe_eintraege_bearbeiten1)
                print()
            while True:
                print('( 1 ) Vorname ändern')
                print('( 2 ) Nachname ändern')
                print('( 3 ) Alter ändern')
                print('( 4 ) Email ändern')
                print('( 5 ) Adresse ändern')
                print('( 6 ) Zurück zum Hauptmenü')
                eingabe_eintraege_bearbeiten2 = int(input('\nEingabe: '))                
                if eingabe_eintraege_bearbeiten2 == 1:
                    vorname_bearbeiten(eingabe_eintraege_bearbeiten1)
                elif eingabe_eintraege_bearbeiten2 == 2:
                    nachname_bearbeiten(eingabe_eintraege_bearbeiten1)
                elif eingabe_eintraege_bearbeiten2 == 3:
                    alter_bearbeiten(eingabe_eintraege_bearbeiten1)
                elif eingabe_eintraege_bearbeiten2 == 4:
                    email_bearbeiten(eingabe_eintraege_bearbeiten1)
                elif eingabe_eintraege_bearbeiten2 == 5:
                    adresse_bearbeiten(eingabe_eintraege_bearbeiten1)
                elif eingabe_eintraege_bearbeiten2 == 6:
                    print()
                    break
            break                        

#%% Einträge löschen

    elif eingabe_hauptmenue == 4:
        while True:
            print('\n-- Einträge löschen: --\n')
            try:
                eingabe_eintraege_loeschen1 = int(input('Bitte zu löschende ID eingeben: '))
            except  ValueError:
                print('Eingabe abgebrochen')
                break
            except:
                print(f'ID {eingabe_eintraege_loeschen1} nicht gefunden !')
                break
            else:
                print()
                id_abfrage(eingabe_eintraege_loeschen1)
                print()
                eingabe_eintraege_loeschen2  = input('Eintrag endgültig löschen ? ( ja / nein ): ')
                if eingabe_eintraege_loeschen2 == 'ja':
                    Register_ID.remove_id(eingabe_eintraege_loeschen1)
                    with open(datenbank_txt_name, 'w') as writer:
                        json.dump(Register_ID.json_pack, writer)
                elif eingabe_eintraege_loeschen2 == 'nein':
                    print(f'Eingabe abgebrochen\n')
                    break
                else:
                    print('Es wird nur -ja- und -nein- als Eingabe akzeptiert !\n')
            break

    elif eingabe_hauptmenue == 5:
        print('Einträge gespeichert !')
        input('- Schließen mitbeliebiger Taste -')
        break