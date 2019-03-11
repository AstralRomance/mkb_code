import os
import xml.etree.ElementTree as xml

class pdf_parser:
    def __init__(self, given_path, pdf_list):
        self.res_dir = given_path
        self.pdf_list = pdf_list
        self.pdf_res = self.pdf_list.copy()
        for i, j in enumerate(self.pdf_res):
            self.pdf_res[i] = j.replace('pdf', 'xml')


    def make_xml_from_pdf(self):
        current_path = self.res_dir + '\\members\\'
        target_path = self.res_dir + '\\xml_temp\\'
        for i in range(len(self.pdf_list)):
            current_path += self.pdf_list[i]
            target_path += self.pdf_res[i]
            os.system('pdf2txt.py -o {0} {1}'.format(target_path, current_path))
        self.parse_temp_xml()

    def parse_temp_xml(self):
        trees_list = []
        for files in os.listdir(self.res_dir + '\\xml_temp\\'):
            tree = xml.parse(files)
            trees_list.append(tree)
            for roots in self.trees_list:
                roots = roots.getroot()


