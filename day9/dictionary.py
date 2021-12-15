'''dictionary = {}

dictionary['superman'] = 'he is very strong'
dictionary['flash'] = 'he is the fastest man over the world '

dictionary.pop('superman')'''


dictionary = {'superman':{'power1':'he can fly','power2':'he is strong'},
'flash':'he is the fastest man over the world',
'green lantern':'he is the chosen one'}

for key in dictionary:
    print(key)
    print(dictionary[key])


