# CART 1
m1m = 0.0
v1b = []
v1a = []
m1b = []
m1a = []
k1b = []
k1a = []

# CART 2
m2m = 0.0
v2b = []
v2a = []
m2b = []
m2a = []
k2b = []
k2a = []

# TOTALS
trials = 4
tmb = []
tma = []
rtm = []
tkb = []
tka = []
rtk = []

# DATA COLLECTION
m1m = float(input('m1m'))
m2m = float(input('m2m'))
for trial in range(1, trials + 1):
    print('Trial ' + str(trial) + ': ')
    v1b.append(float(input('v1b')))
    v2b.append(float(input('v2b')))
    v1a.append(float(input('v1a')))
    v2a.append(float(input('v2a')))


# MOMENTUM BEFORE
# CART 1
for i in range(trials):
    m1b.append(m1m * v1b[i])
print('\n m1b: ')
print(m1b)

#CART 2
for i in range(trials):
    m2b.append(m2m * v2b[i])
print('\n m2b: ')
print(m2b)


# MOMENTUM AFTER
# CART 1
for i in range(trials):
    m1a.append(m1m * v1a[i])
print('\n m1a: ')
print(m1a)

#CART 2
for i in range(trials):
    m2a.append(m2m * v2a[i])
print('\n m2a: ')
print(m2a)

# TOTAL MOMENTUM BEFORE COLLISION
for i in range(trials):
    tmb.append(m1b[i] + m2b[i])
print('\n tmb: ')
print(tmb)

# TOTAL MOMENTUM AFTER COLLISION
for i in range(trials):
    tma.append(m1a[i] + m2a[i])
print('\n tma: ')
print(tma)

# RATIO OF TOTAL MOMENTUM
for i in range(trials):
    rtm.append( tma[i] / tmb[i] )
print('\n rtm: ')
print(rtm)

# KINETIC ENERGY BEFORE
# CART 1
for i in range(trials):
    k1b.append( 0.5 * m1m * v1b[i]**2 )
print('\n k1b: ')
print(k1b)

# CART 2
for i in range(trials):
    k2b.append( 0.5 * m2m * v2b[i]**2 )
print('\n k2b: ')
print(k2b)

# KINETIC ENERGY AFTER
# CART 1
for i in range(trials):
    k1a.append( 0.5 * m1m * v1a[i]**2 )
print('\n k1a: ')
print(k1a)

# CART 2
for i in range(trials):
    k2a.append( 0.5 * m2m * v2a[i]**2 )
print('\n k2a: ')
print(k2a)


# TOTAL KE BEFORE COLLISION
for i in range(trials):
    tkb.append(k1b[i] + k2b[i])
print('\n tkb: ')
print(tkb)

# TOTAL KE AFTER COLLISION
for i in range(trials):
    tka.append(k1a[i] + k2a[i])
print('\n tka: ')
print(tka)

# RATIO OF TOTAL KE
for i in range(trials):
    rtk.append( tka[i] / tkb[i] )
print('\n rtk: ')
print(rtk)
