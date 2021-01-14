puske =["puska ak47","puska m4a1","pistolj glock",]
puske.append("classic pistoil") #dodaje nov element na kraju


puske.insert(4,"kokoska") #kad se stavi na taj broj on stoji na njegovo mesto i pomera se za 1

#a = ' ,'.join(puske)  #join funkcija
puske.remove("puska ak47") #brise tagan element 


puske.clear()#puske.clear() brise sve elemente 

puske.pop() #izbacuje zadnji element ako se pise broj u parametar izbacuje taj red

print(puske) #ispisuje listu 

print(puske.index("pistolj glock"))  #pokazuje na kom broju se nalazi element 
print(puske.count("jabuke"))  #pokazuje koliko puta se ponavlja element


puske.sort() #sortira po azbucnom redu ili ka manjem na vecem broju
puske.reverse() #sortira naopacki 


slatkisi = playstation.copy() #kopira listu u drugu listu

slatkisi.extend(playstation) #duplira listu

print(slatkisi)



                         














