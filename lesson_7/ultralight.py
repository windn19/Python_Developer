from docx.shared import Cm  # импорт из библиотеки класса для обработки изображений
from docxtpl import DocxTemplate, InlineImage
# импорт из библиотеки классов генерации doc документов из шаблонов и включения в них изображений


def get_context(result_sku_list):
    """
    возвращает словарь значений, которые будут отправлены в шаблон
    result_sku_list: данные для отправки в документ
    """
    return {
        'brand': result_sku_list[0],
        'model': result_sku_list[1],
        'sup': result_sku_list[2],
        'price': result_sku_list[3]
    }


def from_template(result_sku_list, template, signature):
    """
    Создание документа и включение в него рисунка
    result_sku_list: данные для передачи в документ
    template: файл шаблона doc-документа
    signature: файл рисунка для документа
    """
    template = DocxTemplate(template)  # создание шаблона документа
    context = get_context(result_sku_list)  # получение данных в виде словаря

    img_size = Cm(8)  # преобразование изображения к нужному размеру
    acc = InlineImage(template, signature, img_size)  # создания объекта класса для вставки в документ

    context['acc'] = acc  # добавление объекта с рисунком в словарь данных
    template.render(context)  # создание шаблона на основе словаря данных

    template.save('rep12.docx')  # сохранение его в файле.


def generate_report(result_sku_list):
    """
    Создание doc-документа для данных
    result_sku_list: данные для передачи в документ
    """
    template = 'repor1.docx'  # шаблон документа
    signature = 'IiGd2vv6-Cc.jpg'  # изображение для вставки в шаблон
    from_template(result_sku_list, template, signature)  # вызов метода для генератора документа


with open('exp.txt', mode='r') as f:  # открытие файла для чтения данных
    data = f.read()  # передача всех данных из файла - как строку.
generate_report(data.split(';'))
# вызов метода для создания документа, разделяя полученные данные по ";" и превращая их в список
