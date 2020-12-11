from docx.shared import Cm  # импорт из библиотеки класса для обработки изображений
from docxtpl import DocxTemplate, InlineImage
# импорт из библиотеки классов генерации doc документов из шаблонов и включения в них изображений
import csv  # подключение библиотеки для работы с csv
import json  # подключение библиотеки для работы с json
from time import time  # импорт метода для работы со временем


def get_context(result):
    """
    возвращает словарь значений, которые будут отправлены в шаблон
    result: данные для отправки в документ
    """
    return {
        'dates': result
    }


def from_template(result, template, signature, outfile):
    """
   Создание документа и включение в него рисунка
   result_sku_list: данные для передачи в документ
   template: файл шаблона doc-документа
   signature: файл рисунка для документа
   outfile: файл для сохранения готового документа
   """
    template = DocxTemplate(template)  # создание шаблона документа
    context = get_context(result)  # получение данных в виде словаря

    img_size = Cm(8)  # преобразование изображения к нужному размеру
    acc = InlineImage(template, signature, img_size)  # создания объекта класса для вставки в документ

    context['acc'] = acc  # добавление объекта с рисунком в словарь данных
    template.render(context)  # создание шаблона на основе словаря данных

    template.save(outfile)  # сохранение его в файле.


def generate_report(result, outfile):
    """
    Создание doc-документа для данных
    result: данные для передачи в документ
    outfile: файл для сохранения готового документа
    """
    template = 'repor1.docx'  # шаблон документа
    signature = 'IiGd2vv6-Cc.jpg'  # изображение для вставки в шаблон
    from_template(result, template, signature, outfile)  # вызов метода для генератора документа


def create_csv(data, file):
    """
    Создание csv файла
    data: данные, которые нужно записать
    file: файл, куда нужно записать данные
    """
    t = time()  # запоминание момента начала работы метода
    with open(file, mode='w') as f:  # открытие файла для записи
        writer = csv.writer(f, delimiter=';')  # создание объекта для записи данных с разделителем ";"
        writer.writerows(data)  # запись данных в файл
    print(f'Writing complete from {round((time() - t) * 100, 2)} миллисекунд')
    # вывод времени работы метода в миллисекундах


def create_json(csv_file, json_file):
    """
    создание json файла из cvs файла
    csv_file: файл источник данных
    json_file: файл получатель данных
    """
    t = time() # запоминание момента начала работы метода
    with open(csv_file, mode='r') as f:  # открытие файла для чтения
        data = csv.DictReader(f, delimiter=';')  # объявление объекта для чтения файла как словарь с разделителем ";"
        data = list(data)  # превращение прочитанных данных в словарь.

    with open('example.json', mode='w') as f:  # открытия файла для чтения
        json.dump(data, f)  # загрузка данных в открытый файл
    print(f'Json done! {round((time() - t) * 100, 2)} миллисекунд')


def gen_report(file, outfile):
    t = time()
    with open(file, mode='r') as f:
        data = json.load(f)
    generate_report(data, outfile)
    print(f'Report generated from {round((time() - t) * 100, 2)} милисекунд')
    # вывод времени работы метода в миллисекундах


car_data = [['brand', 'sup', 'year', 'price'],  # исходные данные
            ['Volvo', 1.5, 2017, 2345],
            ['Lada', 0.5, 2018, 5675],
            ['Audi', 2.0, 2018, 9877]]
infile = 'example.csv'  # файл для сохранения csv
out_file = 'example.json'  # файл для сохранения json

create_csv(car_data, infile)  # вызов метода для создания csv
create_json(infile, out_file)  # вызов метода для создания json
gen_report(out_file, 'rep12.docx')  # создание doc документа
