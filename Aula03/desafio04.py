m = float(input('Digite a metragem: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mi = m * 1000
print('A metragem é de {} metros \n cm = {:.0f} \n mn = {:.0f} \n km = {} \n hm = {} \n dam = {} \n dm = {}'.format(m, cm, mi, km, hm, dam, dm))