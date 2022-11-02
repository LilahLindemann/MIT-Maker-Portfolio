import numpy as np

filename = 'C:/Users/lilah/Downloads/textdoc2.txt'
work = open(filename, encoding='UTF-8')
workstr = ''
charcount = 0
for line in work:
    for i in range(len(line)):
        workstr += line[i]
        charcount += 1
work = workstr

#print(work)
d = {}
hold = ''

k = 8

for i in range(len(work)-k-1):
    hold = work[i:i+k]
    if hold in d:
        if work[i+k] in d[hold]:
            d[hold][work[i+k]] += 1
        else:
            d[hold][work[i+k]] = 1
    else:
        d[hold] = {work[i+k]: 1}

#print(d)

d2 = {}
basis=0
maxes = {}

for key in d.keys():
    d2[key] = {}
    basis=0
    for key2 in d[key]:
        hold = basis+d[key][key2]
        d2[key][hold] = key2
        basis = hold
    maxes[key] = basis

#print(d2)

N = 5000
seed = 'thought '
result = seed
anses = ''

#print('maxes', maxes)

for i in range(N):
    key = result[i:i+k]
    if not(key in maxes):
        break
    num = np.random.random()*maxes[key]
    ans = ''
    for key2 in d2[key]:
        if num < key2:
            ans = d2[key][key2]
            break
    anses += ans
    result += ans

print(result)

print('\n\n************************\n\n')

work = open('C:/Users/lilah/Downloads/textdoc2.txt', encoding='UTF-8').read()
        
work = work.split(' ')
print(work)

#print(work)
d = {}
hold = ''

k = 2



for i in range(len(work)-k-1):
    thing = work[i:i+k]
    #print('thing',thing)
    hold = ''
    for j in range(len(thing)):
        hold += thing[j]
        if j<len(thing)-1:
            hold += ' '
    #print('hold',hold)
    #print('next',work[i+k])
    if hold in d:
        if work[i+k] in d[hold]:
            d[hold][work[i+k]] += 1
        else:
            d[hold][work[i+k]] = 1
    else:
        d[hold] = {work[i+k]: 1}
##print(work)
##print(d)

d2 = {}
basis=0
maxes = {}

for key in d.keys():
    d2[key] = {}
    basis=0
    for key2 in d[key]:
        hold = basis+d[key][key2]
        d2[key][hold] = key2
        basis = hold
    maxes[key] = basis

##print(d2)

N = 200
seed = ['Alice','was']
result = seed
anses = ''

#print('maxes', maxes)

for i in range(N):
    take = result[i:i+k]
    key = ''
    for j in range(len(take)):
        key += take[j]
        if j < len(take)-1:
            key += ' '
    #print('key',key)
    if not(key in maxes):
        break
    num = np.random.random()*maxes[key]
    #print('num',num)
    ans = ''
    for key2 in d2[key]:
        if num < key2:
            ans = d2[key][key2]
            break
    #print('ans',ans)
    result.append(ans)

resultstr = ''
for i in range(len(result)):
    resultstr += result[i]
    resultstr += ' '

print(resultstr)
