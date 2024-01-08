animals=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print('List of animals:',animals)
print('Number of animals:',len(animals))
a=input('I want to find: ')
l = a in animals
if l ==True:
    print('There is',a,'in list of animals')
else:
    print('There is not',a,'in list of animals')