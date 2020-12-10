from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import csv
import json
from time import time


def get_context(result):  # возвращает словарь аргументов
    return {
        'dates': result
    }


def from_template(result, template, signature, outfile):
    template = DocxTemplate(template)
    context = get_context(result)  # gets the context used to render the document

    img_size = Cm(8)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save(outfile)


def generate_report(result, outfile):
    template = 'repor1.docx'
    signature = 'IiGd2vv6-Cc.jpg'
    from_template(result, template, signature, outfile)


def create_csv(data, file):
    t = time()
    with open(file, mode='w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(data)
    print(f'Writing complete from {round((time() - t) * 100, 2)} миллисекунд')


def create_json(csv_file, json_file):
    t = time()
    with open(csv_file, mode='r') as f:
        data = csv.DictReader(f, delimiter=';')
        data = list(data)

    with open(json_file, mode='w') as f:
        json.dump(data, f)
    print(f'Json done! {round((time() - t) * 100, 2)} милисекунд')


def gen_report(file, outfile):
    t = time()
    with open(file, mode='r') as f:
        data = json.load(f)
    generate_report(data, outfile)
    print(f'Report generated from {round((time() - t) * 100, 2)} милисекунд')


car_data = [['brand', 'sup', 'year', 'price'],
            ['Volvo', 1.5, 2017, 2345],
            ['Lada', 0.5, 2018, 5675],
            ['Audi', 2.0, 2018, 9877]]
infile = 'example.csv'
out_file = 'example.json'

create_csv(car_data, infile)
create_json(infile, out_file)
gen_report(out_file, 'rep12.docx')
