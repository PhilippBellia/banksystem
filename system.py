'''
Übung mit Klassen umzugehen
'''
import tkinter

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



if __name__ == "__main__":

    Sitzung = tkinter.Tk()
    Sitzung.title("Login")





    Sitzung.mainloop()

    

