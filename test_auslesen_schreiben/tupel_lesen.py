

database = open("tupel.txt", "r")
namen = []
lines = database.readlines()
for line in lines:
    name = line.split()[0]
    namen.append(name)
    
for name in namen:
    if "Philipp" != name: 
        print("Name ist noch verfügbar")
    else:
        print("Name ist vergeben!")
    

