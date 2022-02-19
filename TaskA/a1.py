from re import U
from tr import tr


with open('ciphertext.txt') as file:
    data = file.read()



alpha = { 
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
    }

# Find letter frequencies of ciphertext
for letter in data:
    try:
        alpha[letter] = alpha[letter] + 1
    except:
        continue

alphasort = {k: v for k, v in sorted(alpha.items(), key=lambda item: item[1])}

print(alphasort)

frequencies = ['e', 't', 'a', 'o', 'i']
dicto = 'ESIARNTOLCDUGPMKHBYFVWZXQJ'
texts = 'ETAOINSHRDLCUMWFGYPBVKXJQZ'
actual = 'ETASNRIOHDLPGBMCFUWYKVJZQX'

print(tr(u'ovymbkrsaenxhztjlcgqpwuifd', actual, data))

#clues: abilities, the, councels, cheats, attitude, spiderlike

'''
original text:

the next day peter finds he is no longer nearsighted and has developed spiderlike abilities 
he can also shoot webs out of his wrists and has quick reflexes superhuman speed and strength 
and a heightened ability to sense danger 

having observed peters changed attitude ben confronts peter over this and counsels him that 
with great power comes great responsibility peter ignores ben and enters an underground wrestling 
tournament to win money with the intention to impress mary jane with a car 

he wins his first match but the promoter cheats him of his earnings when a thief robs the promoters 
office peter allows him to escape in retaliation moments later he finds that ben has been shot and 
killed by a carjacker in the street 

enraged peter pursues the carjacker only to learn that bens killer is the thief he let escape 
the carjacker tries to flee but is killed after he falls out of a window

the goblin abducts and offers peter a place at his side but peter refuses during thanksgiving 
dinner norman sees peters wound from a fight the previous day and realizes that he is spiderman 

as revenge the goblin begins to strike at his loved ones hospitalizing may and taking mary jane 
hostage alongside a tramcar full of children at queensboro bridge he tells peter to choose whether 
to save mj or the children but peter manages to save both with some help from bystanders


'''