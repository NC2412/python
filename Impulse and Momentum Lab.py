impulse1 = [-0.59, -0.39, -0.45]
mass1 = 0.518
momentum1 = []
difference1 = []
impulse2 = [-0.497, -1.12, -0.89]
mass2 = 1.037
momentum2 = []
difference2 = []


for i in impulse1:
    momentum1.append(mass1 * i)
print(momentum1)
for i in impulse2:
    momentum2.append(mass2 * i)


for j in range(0,3):
    a = impulse1[j]
    b = momentum1[j]

    diff = ((b-a) / ((b+a) / 2)) * 100
    print(diff)
