import random
from matplotlib import pyplot as plt
plt.style.use("ggplot")

num_sims = 10000
profs = []
for _ in range(num_sims):
    b = 1000
    w_and_ls = [3.75 if (random.randint(1, 6) +
                         random.randint(1, 6)) > 9
                else -1 for _ in range(100)]

    end_bal = [b:= b + i for i in w_and_ls][-1]
    profs.append(end_bal - 1000)

plt.hist(profs, bins=30)
