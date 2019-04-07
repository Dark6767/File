import random
with open("C:/text.txt",mode='w') as text:
    range = range(1,10000)
    for r in range:
        text.write(str(random.randint(0,9))+'\n')