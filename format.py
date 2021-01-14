queue = []
 
queue.append('DOWN') # enqueue
 
queue.append('UP') # enqueue
 
queue.append('A') # enqueue
 
queue.append('B') # enqueue
  
print("Number of commands in queue: {}".format(len(queue))) # size
 
command = queue.pop(0) # dequeue
 
print("Next commands is {}".format(command))
 
command = queue.pop(0) # dequeue
 
print("Next command is {}".format(command))
 
print("Nbr of commands in queue: {}".format(len(queue)))

print('======================================================================')

a = ['h','l','o','w','r','d']
 
b = ['e','l',' ','o','l','']
 
for i in range(len(a)):
 
     print("{}{}".format(a[i], b[i]), end = '')
print('======================================================================')


languages = ['German', 'Spanish', 'French']
for items in range(len(languages)):
    print("Language on index {}, is = {}".format(items, languages[items]))

print('======================================================================')
person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)


sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)
# u slucaju sa keys 

print('======================================================================')
tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
print('======================================================================')

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)


# pi = 3.14159265

# sentence = 'Pi is equal to {}'.format(pi)

# print(sentence)


sentence = '1 MB is equal to {} bytes'.format(1000**2)

print(sentence)


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)



# print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

