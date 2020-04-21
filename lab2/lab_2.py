import matplotlib.pyplot as plt
import csv
# Читаем файл
file = open("nfcapd2.txt")
readFile = csv.reader(file)
# Подсчёт трафика абонента
trafic = 0
listTime = []
listBytes = []
for line in readFile:
    if '77.74.181.52' in line[5] or '77.74.181.52' in line[6]:
        trafic += int(line[9])
        listTime.append(line[1])
        listBytes.append(line[9])
totalCost = trafic / 1024 / 1024 * 1.5
print('%.2f' % totalCost, 'Рублей')
# убираем значение миллисекунд во времени
for i in range(len(listTime)):
    listTime[i] = listTime[i][:listTime[i].find('.')]
# складываем кол-во потраченных байт в одно время (исключая различия в миллисекунды)
summ = 0
for i in range(len(listTime)):
    if i + 1 >= len(listTime):
        break
    while listTime[i] == listTime[i+1]:
        summ = int(listBytes[i]) + int(listBytes[i + 1])
        listBytes[i] = summ
        listBytes.pop(i+1)
        listTime.pop(i+1)
        if i + 1 >= len(listTime):
            break
    summ = 0
# убираем последнию пару, отличающуюся только на миллисекунды
count = 0
def pairs(n):
    for i in range(n):
        for k in range(i+1, n):
            yield i, k
for i, k in pairs(len(listTime)):
    if listTime[i] == listTime[k]:
        summ = int(listBytes[i]) + int(listBytes[k])
        listBytes[i] = summ
        listBytes.pop(k)
        listTime.pop(k)
        count += 1
        break
# постороение графика
plt.title('Трафик')
plt.xlabel('Время')
plt.ylabel('Использованные байты')
plt.scatter(listTime, listBytes)
plt.xticks(listTime, rotation='vertical')
plt.show()

