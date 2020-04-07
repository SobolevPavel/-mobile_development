import csv

# Читаем csv файл
input_file = open("data.csv")
reader = csv.reader(input_file)

# Задаем переменные для подсчётов
sms = 0
originCall = 0
destCall = 0

# Считаем кол-во смс и входящих/исходящих минут
for line in reader:
    if line[1] == '933156729':
        sms += float(line[4])
        originCall += float(line[3])
    if line[2] == '933156729':
        destCall += float(line[3])

# Тарификация CDR
smsCost = 0
if sms > 10:
    smsCost = (sms - 10) * 5
destCallCost = destCall * 4
if originCall >= 10:
    originCallCost = 10 * 2
else:
    originCallCost = originCall * 2

# Считаем общую стоимость
totalCost = smsCost + originCallCost + originCallCost
print(totalCost)





