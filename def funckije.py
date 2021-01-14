def sayhi():       # def funkcija
    print("hello user ")  #mora biti pored slova ili kod ne radi



sayhi()   #odazivanje funkcije  #kad se odaziva kod se vraca na funkciju pa ocitava drugu liniju

print("----------------------------------------------------------------------------------------")


def dobrodosli (name):     #stvar unutar (): se zove parametar       
    print("hello " + name) 

dobrodosli("Kec")       #funkciju smo odazvali i u zagradi () pisemo parametar  
                        #[ako ne pisemo dobijamo error]
dobrodosli("Jelka")

dobrodosli("Keco")
print("----------------------------------------------------------------------------------------")


def ime_godine (name,age):      
    print("hello " + name + ",u are" +age +" years old") #ovde napisemo sta ce da printa

ime_godine("Kec"," 14")       #kec name 14,age

ime_godine("Jelka" ," 42")

ime_godine("srdja"," 45")