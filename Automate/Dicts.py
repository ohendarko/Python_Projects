import random
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print("spam == bacon: {}".format(spam == bacon))
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print("eggs == ham: {}".format(eggs == ham))

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
for k, v in spam.items():
    print("{}:{}".format(k, v))
print(spam.keys())
print(list(spam.keys()))
print(list(spam.items()))

print()

print('name' in spam.keys())
print('color' in spam.keys())
print('name' not in spam.keys())
print('name' in spam)
print(42 in spam)
print(42 in spam.values())

print()

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', "N/A")) + ' eggs.')
spam.setdefault('name', 'Pooka')
print(spam)
spam.setdefault('color', 'white')
print(spam)