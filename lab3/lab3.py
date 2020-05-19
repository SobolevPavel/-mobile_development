from fpdf import FPDF

#Данные из первой и второй лабораторной работы
callCost = 461.76
smsCost = 315.00
internetCost = 0.08
totalCost = callCost + smsCost + internetCost
nds = totalCost * 0.2

#Создание и подготовка файла и шрифтов
pdf = FPDF()
pdf.add_page()
pdf.add_font('Arial', '', 'C:\\Windows\\Fonts\\arial.ttf', True)
pdf.add_font('Arial Bold', '', 'C:\\Windows\\Fonts\\arialbd.ttf', True)

# Верхняя таблица
pdf.set_font('Arial', '', 10)
pdf.cell(85, 15, '', 1, 0)
pdf.cell(-85)
pdf.cell(85, 5, 'АО "БАНК ЗАПЯТАЯ"', 0, 0)
pdf.cell(20, 20, '', 1, 0)
pdf.cell(-20)
pdf.cell(20, 5, 'БИК', 1, 0)
pdf.cell(75, 20, '', 1, 0)
pdf.cell(-75)
pdf.cell(75, 5, '024736713', 0, 1)
pdf.cell(85)
pdf.cell(20, 5, 'Сч. №', 0, 0)
pdf.cell(75, 5, '3003509375639057312', 0, 1)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(85, 5, 'Банк получателя', 1, 1)
pdf.cell(85, 25, '', 1, 0)
pdf.cell(-85)
pdf.cell(42, 5, 'ИНН   '+'579385739012', 1, 0)
pdf.cell(43, 5, 'КПП   '+'780931275534', 1, 0)
pdf.cell(20, 25, '', 1, 0)
pdf.cell(-20)
pdf.cell(20, 5, 'Сч. №', 0, 0)
pdf.cell(75, 25, '', 1, 0)
pdf.cell(-75)
pdf.cell(75, 5, '580964373127863412', 0, 1)
pdf.cell(85, 5, 'ПАО "МТС"', 0, 1)
pdf.cell(0, 10, '', 0, 1)
pdf.cell(85, 5, 'Получатель', 1, 1)

# Заголовок счета
pdf.set_font('Arial Bold', '', 14)
pdf.cell(180, 10, 'Счет №1337 от 19 мая 2020 г.', 0, 1, 'C')
pdf.cell(180, 0.2, '', 1, 1)

# Счет
pdf.set_font('Arial', '', 10)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(30, 5, 'Поставщик', 0, 0)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(140, 5, 'ПАО "МТС",ИНН 785127598, КПП 3097535613, 15666832 г. Москва, ул. Пионера, д. 63', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(30, 5, '(Исполнитель):', 0, 1)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(30, 5, 'Покупатель', 0, 0)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(140, 5, 'Ковальчук Сергей Михайлович, ИНН 57312095221 г. Санкт-Петербург', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(30, 5, '(Заказчик):', 0, 1)
pdf.cell(0, 5, '', 0, 1)
pdf.cell(30, 5, 'Основание', 0, 0)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(140, 5, 'Договор №263216286534 от 14.02.2010', 0, 1)
pdf.cell(0, 5, '', 0, 1)

# Нижняя таблица
pdf.cell(10, 10, '№', 1, 0, 'C')
pdf.cell(90, 10, 'Наименование работ, услуг', 1, 0, 'C')
pdf.cell(20, 10, 'Кол-во', 1, 0, 'C')
pdf.cell(15, 10, 'Ед.', 1, 0, 'C')
pdf.cell(20, 10, 'Цена', 1, 0, 'C')
pdf.cell(25, 10, 'Сумма', 1, 1, 'C')

pdf.set_font('Arial', '', 10)
pdf.cell(10, 5, '1', 1, 0, 'C')
pdf.cell(90, 5, 'Звонки', 1, 0)
pdf.cell(20, 5, '1', 1, 0, 'R')
pdf.cell(15, 5, '1', 1, 0, 'R')
pdf.cell(20, 5, "{:.2f}".format(callCost), 1, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(callCost), 1, 1, 'R')

pdf.cell(10, 5, '2', 1, 0, 'C')
pdf.cell(90, 5, 'СМС', 1, 0)
pdf.cell(20, 5, '1', 1, 0, 'R')
pdf.cell(15, 5, '1', 1, 0, 'R')
pdf.cell(20, 5, "{:.2f}".format(smsCost), 1, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(smsCost), 1, 1, 'R')

pdf.cell(10, 5, '3', 1, 0, 'C')
pdf.cell(90, 5, 'Интернет', 1, 0)
pdf.cell(20, 5, '1', 1, 0, 'R')
pdf.cell(15, 5, '1', 1, 0, 'R')
pdf.cell(20, 5, "{:.2f}".format(internetCost), 1, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(internetCost), 1, 1, 'R')

#Итог
pdf.cell(0, 5, '', 0, 1)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(135)
pdf.cell(20, 5, 'Итого: ', 0, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(totalCost), 0, 1, 'R')

pdf.cell(135)
pdf.cell(20, 5, 'В том числе НДС: ', 0, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(nds), 0, 1, 'R')

pdf.cell(135)
pdf.cell(20, 5, 'Всего к оплате: ', 0, 0, 'R')
pdf.cell(25, 5, "{:.2f}".format(totalCost), 0, 1, 'R')

pdf.cell(0, 5, '', 0, 1)
pdf.set_font('Arial', '', 10)
pdf.cell(180, 5, 'Всего наименований '+'3, на сумму 776.84 руб.', 0, 1)

pdf.set_font('Arial Bold', '', 10)
pdf.cell(180, 5, 'Семьсот семьдесят шесть рублей 84 копейки', 0, 1)

pdf.set_font('Arial', '', 10)
pdf.cell(180, 5, '', 0, 1)
pdf.cell(180, 5, 'Внимание!', 0, 1)
pdf.cell(180, 5, 'Оплата данного счета означает согласие с условиями поставки товара.', 0, 1)
pdf.cell(180, 5, 'Уведомление об оплате обязательно, в противном случае не гарантируется наличие товара на складе.', 0, 1)
pdf.cell(180, 5, 'Товар отпускается по факту прихода денег на р/с Поставщика, самовывозом, при наличии доверенности и', 0, 1)
pdf.cell(180, 5, 'паспорта.', 0, 1)
pdf.cell(180, 5, '', 0, 1)
pdf.cell(180, 5, '', 0, 1)
pdf.cell(180, 0, '', 1, 1)

pdf.cell(180, 0.2, '', 1, 1)
pdf.set_font('Arial Bold', '', 10)
pdf.cell(170, 20, 'Руководитель   _____________________________________         Бухгалтер   _________________________', 0, 1)

pdf.output('Счет на оплату услуг.pdf')
