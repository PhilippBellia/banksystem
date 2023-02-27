'''
Übung mit Klassen umzugehen
'''
import tkinter
import hashlib as h
import bcrypt

class Konto:
    
    saldo = 0 

    def kontostand_abfragen(self):
        print(f"Dein Saldo beträgt: {self.saldo} €")

    def guthaben_hinzufügen(self, betrag):
        self.saldo += betrag
        print(f"Dein neues Saldo beträgt: {self.saldo} €")
    
    def geld_abbuchen(self, betrag):
        
        if self.saldo >= betrag:
            self.saldo -= betrag
            print(f"{betrag} € abgebucht. \nNeues Saldo: {self.saldo} €")
        else:
            print(f"Du hast nicht genügend Geld um diese Überweisung zu tätigen! \nAktuelles Saldo: {self.saldo} €")
    

def fenster_schliessen():
    Sitzung.destroy()

def pw_hash(pw_as_string):
# String muss aber encoded sein 
    salt = bcrypt.gensalt()
    h = bcrypt.hashpw(pw_as_string, salt)
    return h


def anmelden():
    anmelde_file = open("anmelde_file.txt", "r")

    namen = []
    zeilen = anmelde_file.readlines()
    print(type(zeilen))
    if zeilen:    
        for zeile in zeilen:
            name = zeile.split()[0]
            namen.append(name)
    anmelde_file.close()

    for name in namen:
        if eingabe_1.get() == name:
            passwort = eingabe_2.get()
            passw_hash = pw_hash(passwort.encode("utf-8"))
            print(passw_hash)
            anmelde_file = open("anmelde_file.txt", "r")
            passwoerter = []
            rows = anmelde_file.readlines()
            if rows:
                for row in rows:
                    passwort = row.split()[1]
                    passwoerter.append(passwort)
            anmelde_file.close()

            for pw in passwoerter:
                if pw == passw_hash:
                    print("Eingeloggt")
                    return 0
            print("Falsches Passwort oder Benutzername")
           


def registrieren():

    def fenster_schliessen_2():
        registrationsfenster.destroy()

    def registration():
        # Check ob Name bereits vergeben ist ######################################################
        account_file = open("anmelde_file.txt", "r")
        namen = []
        zeilen = account_file.readlines()
        print(type(zeilen))
        if zeilen:    
            for zeile in zeilen:
                name = zeile.split()[0]
                namen.append(name)

            for name in namen:
                if namen_eingabe.get() == name: 
                    print("Benutzer ist bereits vergeben, bitte anderen Namen waehlen! ")
                    return 0
        else: 
            print("Liste ist leer")
        account_file.close()
        print("Benutzername ist verfügbar!")
        ############################################################################################

        # Passwort aus Eingabefeld nehmen, hashen und Hash printen #################################
        pw_ = pw_hash(str(passwort_eingabe.get()).encode("utf-8"))
        print("PW-Hash: ", pw_)
        ############################################################################################
        
        # Benutzer als Tupel sichern und in eine Datei hineinschreiben #############################
        neuer_benutzer = (str(namen_eingabe.get()), pw_)

        benutzer_hinzufügen = open("anmelde_file.txt", "a")
        for benutzer in neuer_benutzer:
            benutzer_hinzufügen.write(str(benutzer) + " ")
        benutzer_hinzufügen.write("\n")

        benutzer_hinzufügen.close()
        #############################################################################################

    # Registrationsfenster ##########################################################################
    registrationsfenster = tkinter.Toplevel(Sitzung)
    registrationsfenster.geometry("400x200")
    registrationsfenster.title("Registrationsfenster")

    namen_label = tkinter.Label(registrationsfenster, text="Benutzername")
    namen_label.pack()

    namen_eingabe = tkinter.Entry(registrationsfenster)
    namen_eingabe.pack()
    

    passwort_label = tkinter.Label(registrationsfenster, text="Passwort festlegen:")
    passwort_label.pack()

    passwort_eingabe = tkinter.Entry(registrationsfenster, text="Passwort sicher bestimmen")
    passwort_eingabe.pack()

    registrieren_button = tkinter.Button(registrationsfenster, text="Registrieren", command=registration)
    registrieren_button.pack()

    registrationsfenster_beenden = tkinter.Button(registrationsfenster, text="Schließen", command=fenster_schliessen_2)
    registrationsfenster_beenden.pack()
    ##################################################################################################

    




if __name__ == "__main__":

    
    Sitzung = tkinter.Tk()
    Sitzung.geometry("300x200+100+100")
    Sitzung.title("Login")
    

    benutzer = tkinter.Label(Sitzung, text="Benutzername:")
    benutzer.grid(row=0, column=0)

    passwort = tkinter.Label(Sitzung, text="Passwort:")
    passwort.grid(row=1, column=0)

    eingabe_1 = tkinter.Entry(Sitzung, text="Benutzername")
    eingabe_1.grid(row=0, column=1)
    eingabe_2 = tkinter.Entry(Sitzung, text="Passwort")
    eingabe_2.grid(row=1, column=1)

    schließen = tkinter.Button(Sitzung, text="Beenden", command=fenster_schliessen)
    schließen.grid(row=2)

    anmelden_button = tkinter.Button(Sitzung, text="Anmelden", command=anmelden)
    anmelden_button.grid(row=2, column=1)
    registrieren_button = tkinter.Button(Sitzung, text="Registrieren", command=registrieren)
    registrieren_button.grid(row=2, column=2)

    Sitzung.mainloop()

    


