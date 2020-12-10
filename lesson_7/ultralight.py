from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(result_sku_list): # возвращает словарь аргуменов
    return {
        'brand': result_sku_list[0],
        'model': result_sku_list[1],
        'sup': result_sku_list[2],
        'price': result_sku_list[3]
    }


def from_template(result_sku_list, template, signature):
    template = DocxTemplate(template)
    context = get_context(result_sku_list)  # gets the context used to render the document

    img_size = Cm(8)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save('rep12.docx')


def generate_report(result_sku_list):
    template = 'repor1.docx'
    signature = 'IiGd2vv6-Cc.jpg'
    from_template(result_sku_list, template, signature)


with open('exp.txt', mode='r') as f:
    data = f.read()
generate_report(data.split(';'))
