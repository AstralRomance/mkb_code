from xml_to_text_parse import *
from pdf_parse import *
import os

path = os.getcwd()# Верхняя директория проекта, из нее ходить по всем папкам
files_list = []
xml_list = []
pdf_list = []
files_list = os.listdir(path=path+'\\members')
for i in files_list:
    if 'xml' in i:
        xml_list.append(i)
    else:
        pdf_list.append(i)
# Парсинг xml в txt
os.chdir(path+'\\members')
prs = xml_parse(path, xml_list)
prs.get_file_list()


# Парсинг pdf в txt
pdf_prs = pdf_parser(path, pdf_list)
pdf_prs.make_xml_from_pdf()