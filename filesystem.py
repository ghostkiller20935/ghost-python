with open ('kec.txt', 'r+') as f:
    c = f.readlines()
with open ('kec.txt', 'w') as f:
    for i in c:
        f.write(i)
        print("=")


print(i)