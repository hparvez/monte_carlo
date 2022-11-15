import random
from matplotlib import pyplot as plt
plt.style.use("ggplot")

p = []

for si in range(10000):
    b = 1000
    b2 = []
    for ri in range(100):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        t = d1 + d2
        if t > 9:
            b = b + 3.75
            b2.append(b)
        else:
            b = b - 1
            b2.append(b)
    pi = b2[-1]
    p.append(pi)

for i in range(len(p)):
    p[i] = p[i] - 1000

plt.hist(p, bins=30)
