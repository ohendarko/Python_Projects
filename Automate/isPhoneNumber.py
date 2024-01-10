import re
import _sre
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainLine = mo.groups()
print(areaCode)
print(mainLine)

print('='*30)
print('Matching Multiple Groups with the Pipe')
print('Program Output:')
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

print('*'*20)
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))

print('='*30)
print('Optional Matching with the Question Mark')
print('Program Output:')
batRegex2 = re.compile(r'Bat(wo)?man')
mo4 = batRegex2.search('The Adventures of Batman')
print(mo4.group())
mo5 = batRegex2.search('The Adventures of Batwoman')
print(mo5.group())

print('='*30)
print('Matching Zero or More with the Star')
print('Program Output:')
batRegex3 = re.compile(r'Bat(wo)*man')
mo6 = batRegex3.search('The Adventures of Batman')
print(mo6.group())
mo6 = batRegex3.search('The Adventures of Batwoman')
print(mo6.group())
mo6 = batRegex3.search('The Adventures of Batwowowowoman')
print(mo6.group())

print('='*30)
print('Matching One or More with the Plus')
print('Program Output:')
batRegex3 = re.compile(r'Bat(wo)+man')
try:
    mo6 = batRegex3.search('The Adventures of Batman')
    print(mo6.group())
except AttributeError:
    print('''No match found for Bat(wo)+man in 'The Adventures of Batman':
No instance of 'wo' found. At least 1 required.
''')
mo6 = batRegex3.search('The Adventures of Batwoman')
print(mo6.group())
mo6 = batRegex3.search('The Adventures of Batwowowowoman')
print(mo6.group())

print('='*30)
print('Greedy and Nongreedy Matching')
print('Program Output:')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

print('='*30)
print('The findall() Method')
print('Program Output:')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

print('='*30)
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))

print('='*30)
print('Case-Insensitive Matching')
print('Program Output:')
robocop = re.compile(r'robocop', re.IGNORECASE)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

print('='*30)
print('Substituting Strings with the sub() Method')
print('Program Output:')
namesRegex = re.compile(r'Agent \w+')
subbed = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(subbed)
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

print('*'*20)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))