'''
LEGB
Local,Enclosing,Global,Bulid-in
'''


x="global x"    #global


print('--------------------------------------------')
m =min([3,4,6,7,8,2,4,5])   #bulit in
print(m)
print('--------------------------------------------')
def test():
    y="local y"  #local je samo u funkciju 
    print(y)
 

test()
print('--------------------------------------------')
def kec(z):
    y="local y" 
    
    print(z)
 

kec('local z')

print('--------------------------------------------')

def outer():
    x="outer x" #enclosing

    def inner():
        x='inner x'
        print(x)
    inner()
    print(x) #enclosing

outer()