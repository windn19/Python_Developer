import csv
from docxtpl import DocxTemplate

temple = DocxTemplate('report1.docx')
with open('example.csv', mode='r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    # for row in reader:
    context = {'lines': reader}
    temple.render(context)
temple.save('rep1.docx')
