arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
def party_late(arrivals,name):
    if name==arrivals[-1]:
        return False
    elif name==arrivals[0]:
        return False
    elif name==arrivals[1]:
        return False
    elif name==arrivals[2]:
        return False
    elif name==arrivals[3]:
        return False
    else:
        return True
print(party_late(arrivals,name='Gilber'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))