import random

for i in range(3):
    print(random.randint(10,20))

members = ['John', 'May', 'Jay','Bob']
leader = random.choice(members)
print(leader)
