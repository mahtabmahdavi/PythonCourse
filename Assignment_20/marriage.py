import random

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]
marriage = []

for i in range(min(len(boys), len(girls))):
    random_boy = random.choice(boys)
    boys.remove(random_boy)
    random_girl = random.choice(girls)
    girls.remove(random_girl)
    marriage.append((random_boy, random_girl))

print(marriage)