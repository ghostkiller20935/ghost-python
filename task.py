string="2,0,9,3,5"
list=string.split(",")
list2=[]
string2=""
for items in list:
    list2.append(str(int(items)**2))
    string2=",".join(list2)
print(list2)


    #od stringa "2,0,9,3,5,2020" napravi u listu mnozi sa 2 i da output vude string  