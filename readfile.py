
import math
s=0
l=0
with open("C:/text.txt",mode='r') as text:
    for line in text:
        a=int(line)
        s += a
        l += 1
    print(str(s / l))