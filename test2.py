string = "3,9,13,4,42"
list = string.split(",")
list2 = []
for x in list:
    list2.append(str(int(x) ** 2))
string2 = ",".join(list2)
 

print("string= " +string2)


