
broj1 = int(input("enter first number:"))
op = input ('enter operator:')
broj2 = int(input("enter second number:"))
if op =="+":
    print (broj1 + broj2)
elif op=="-":
    print (broj1 - broj2)
elif  op== "*":
    print (broj1 * broj2) 
elif op== '/':
    print (broj1 / broj2)
else: 
    print("invalid operator")