# Читаем файл
with open("nfcapd.csv", 'r') as file:
    reader = file.read()
# Разделяем исходный текст запятыми, для чтения с формата csv
text = ''
count = 0
for line in reader:
    if line == ' ' and count == 0:
        text += ', '
        count = 1
        continue
    if line != '-' and line != '>' and line != ' ':
        count = 0
        text += line
# Запись получившегося текста в файл
with open('nfcapd2.txt', 'w') as file2:
    for line in text:
        file2.write(line)
    file2.close()
