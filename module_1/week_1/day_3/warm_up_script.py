from __future__ import division

people = {'Charles': [23.4, "Darwin"], 'Alan': [42.5, "Turing"], 'Albert': [69, "Einstein"], 
          'Max': [81, "Planck"], 'Richard': [67, "Feynman"]}

people.pop('Charles')

people['Max'][0] = 52

ages = []
for key in people:
    print(people[key][1])
    ages.append(people[key][0])

print(ages)

mean = 0

for age in ages:
    mean = mean + age
    
print(mean)  