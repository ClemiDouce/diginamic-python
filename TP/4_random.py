import random

print(random.randint(1,10))
print(random.randrange(1,100))
ma_liste = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(ma_liste))
random.shuffle(ma_liste)
print(ma_liste)