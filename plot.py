import matplotlib.pyplot as plt

file = open("../Testes/1/tst.txt", "r")

fitness = []

for x in file:
    fitness.append(int(x))

print(len(fitness))

count = list(range(len(fitness)))

print(len(count))
print(len(fitness))

plt.plot(count, fitness)
plt.show()
