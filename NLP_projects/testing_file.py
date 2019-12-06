places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listfile555.csv', 'w') as filehandle:
    for listitem in places:
        filehandle.write('%s\n' % listitem)
