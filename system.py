'''
Übung mit Klassen umzugehen
'''
import tkinter
import hashlib as h

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

def anmelden():
    anmelde_file = open("Accounts.txt", "r")
    accounts = anmelde_file.readline(1)
    print(accounts)

def registrieren():
    pass

if __name__ == "__main__":

    Sitzung = tkinter.Tk()
    Sitzung.title("Login")

    benutzer = tkinter.Label(Sitzung, text="Benutzername:").grid(row=0, column=0)
    passwort = tkinter.Label(Sitzung, text="Passwort:").grid(row=1, column=0)

    eingabe_1 = tkinter.Entry(Sitzung, text="Benutzername" ).grid(row=0, column=1)
    eingabe_2 = tkinter.Entry(Sitzung, text="Passwort").grid(row=1, column=1)

    schließen = tkinter.Button(Sitzung, text="Beenden", command=fenster_schliessen).grid(row=2)
    anmelden_button = tkinter.Button(Sitzung, text="Anmelden", command=anmelden).grid(row=2, column=1)
    registrieren_button = tkinter.Button(Sitzung, text="Registrieren", command=registrieren).grid(row=2, column=2)

    Sitzung.mainloop()

    

