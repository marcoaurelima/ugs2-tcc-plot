
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')

file = open("../Testes/1/logs/fitness-log.txt", "r")

fitnessMin = 31

fitness = []

for x in file:
    if(int(x) - fitnessMin < 0):
        continue
    fitness.append(int(x) - fitnessMin)

count = list(range(len(fitness)))

plt.plot(count, fitness)
plt.show()


