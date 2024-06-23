from PyPDF2 import PdfReader, PdfWriter


def generate_watermark(file_name):
    template = PdfReader(open(f'{file_name}.pdf', 'rb'))
    watermark = PdfReader(open('wtr.pdf', 'rb'))
    output = PdfWriter()
    file_name = open(f'{file_name}.pdf', 'r')

    for i in range(len(template.pages)):
        page = template.pages[i]
        page.merge_page(watermark.pages[0])
        output.add_page(page)

        with open(f'{file_name.name.removesuffix('.pdf')}_watermarked.pdf', 'wb') as file:
            output.write(file)
