#for [loop pocinje sa for]
#letter [moze da se pise bilo sta ovde je primer letter]
#in 
# "****" pisemo koj variale da loopa
#print (letter) pisemo komandu na loopa

#za svako slovo u crni kec ocu da printujem ta slova

for letter in "crni kec":   
    print(letter)
print("------------------------------------------------------------")

voce=['leba','pirinac','meso','burek']

for items in voce:
    print(items)
print("------------------------------------------------------------")

#za broj od 0,10 printuj broj
for broj in range(10):
    print(broj)
print("------------------------------------------------------------")
#za broj od 3 do 6 printtuj broj
for number in range(3,6):
    print(number)
print("------------------------------------------------------------")


#auto=['ferrari','lamborgini','golf','bmw']          (je lista)
#za items u  range(len(auto)):
#ispisi (auto [items]) 
#  [len je komanda koja ispisuje koliko stvari se nalazi u listi] 
auto=['ferrari','lamborgini','golf','bmw']
for items in range(len(auto)):
    print(auto[items])

print("------------------------------------------------------------")

setup=['mis','tastatura','komp','monitor','podloga']
for items in range(len(setup)):
    print(setup[items])
    
print("------------------------------------------------------------")



#za stvaru do broja 5 
#ako je srvar jednak 0 ispisi prva iteracija
#ostalo ispisi nije prva iteracija

for stvari in range (5):
    if stvari==0:
        print("prva iteracija")
    else:
        print("nije prva iteracija")