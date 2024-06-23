from PyPDF2 import PdfWriter
from pdf_find_master import fill_folder
import os

dir_folder = os.listdir('./pdfs')


def merge_pdf():
    set_file_name = input(f'Enter PDF\'s name: ')
    file_name = set_file_name

    merger = PdfWriter()

    pdf_list = fill_folder(dir_folder)

    for i in pdf_list:
        merger.append(i)

    output = open(f'{file_name}.pdf', 'wb')
    merger.write(output)

    merger.close()
    output.close()

    return file_name
