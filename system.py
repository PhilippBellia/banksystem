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

    salt = bcrypt.gensalt()
    h = bcrypt.hashpw(pw_as_string, salt)
    return h


def anmelden():
    anmelde_file = open("Accounts.txt", "r")
    for line in anmelde_file.read():
        if str(eingabe_1) == line:
            keys = open("pass.txt", "r")
            pw = str(eingabe_2)
            for o_line in keys.read():
                test_ob_pw_richtig = bcrypt.compare(pw, o_line)
                if test_ob_pw_richtig == True:
                    return True
                else:
                    continue
        else:
            print("Falscher Benutzername")
            return False



def registrieren():

    def fenster_schliessen_2():
        registrationsfenster.destroy()

    def registration():
        account_file = open("Accounts.txt", "r")
        for line in account_file.read():
            if line == str(namen_eingabe):
                print("Name ist bereites vergeben!")
                return print("Error, Eingabe wiederholen")
            else:
                continue

        pw_ = pw_hash(str(passwort_eingabe))

        pw_file = open("pass.txt", "r")
        for paw in pw_file.read():
            if paw == pw_:
                print("anderes Passwort festlegen")
                return print("Error")
            else:
                continue



        account_file.close()
        account_file = open("Accounts.txt", "p")
        account_file.write("\n" + str(namen_eingabe))




    registrationsfenster = tkinter.Toplevel(Sitzung)

    namen_label = tkinter.Label(registrationsfenster, text="Benutzername").pack()
    namen_eingabe = tkinter.Entry(registrationsfenster).pack()

    passwort_label = tkinter.Label(registrationsfenster, text="Passwort festlegen:").pack()
    passwort_eingabe = tkinter.Entry(registrationsfenster, text="Passwort sicher bestimmen").pack()

    registrieren_button = tkinter.Button(registrationsfenster, text="Registrieren", command=registration).pack()

    registrationsfenster_beenden = tkinter.Button(registrationsfenster, text="Schließen", command=fenster_schliessen_2).pack()


    anmelde_file = open("Accounts.txt", "r")
    #for line in anmelde_file.read():




if __name__ == "__main__":

    print("hallo")
    Sitzung = tkinter.Tk()
    Sitzung.geometry("300x400+30+30")
    Sitzung.title("Login")
    

    benutzer = tkinter.Label(Sitzung, text="Benutzername:").grid(row=0, column=0)
    passwort = tkinter.Label(Sitzung, text="Passwort:").grid(row=1, column=0)

    eingabe_1 = tkinter.Entry(Sitzung, text="Benutzername").grid(row=0, column=1)
    eingabe_2 = tkinter.Entry(Sitzung, text="Passwort").grid(row=1, column=1)

    schließen = tkinter.Button(Sitzung, text="Beenden", command=fenster_schliessen).grid(row=2)
    anmelden_button = tkinter.Button(Sitzung, text="Anmelden", command=anmelden).grid(row=2, column=1)
    registrieren_button = tkinter.Button(Sitzung, text="Registrieren", command=registrieren).grid(row=2, column=2)

    Sitzung.mainloop()

    



