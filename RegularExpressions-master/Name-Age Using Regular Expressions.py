import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)


x=0

##for (x=0; x<ages.length(), x++):
##    print(ages[x])


ageDictionary = {}


for eachName in names:
    ageDictionary[eachName] = ages[x]
    x+=1

print(ageDictionary)
