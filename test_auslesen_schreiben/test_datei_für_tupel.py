

anmelde_tupel = ("Philipp", "wdfkjghworg1213")

database = open("tupel.txt", "a")
print("Datei geöffnet...")

for t in anmelde_tupel:
    database.write(t + " ")
print("Tupel eingetragen...")

database.write("\n")
database.close()

print ("Ende!")