import matplotlib.pyplot as plt

file = open("../Testes/1/tst.txt", "r")

fitness = []

for x in file:
    fitness.append(int(x))

count = list(range(len(fitness)))

plt.plot(count, fitness)
plt.show()
