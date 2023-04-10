#let's create a simple dictionary
phones = {'politsei':'110', 'kiirabi':'112', 
'koolidirektor':'6285200'}

#get element by key
print("Politsei number on " + phones['politsei'])

#check if key exists in the dictionary
if 'ema' in phones:
    print("Ema telefoninumber on " + phones['ema'])
else:
    print("Ma ei tea ema numbrit")

#loop through dictionary elements
for name in phones:
    print(name.capitalize() + ' - ' + phones[name])

#add elements to dictionary
print(phones)
phones['ema'] = '656561564'
print(phones)

input()