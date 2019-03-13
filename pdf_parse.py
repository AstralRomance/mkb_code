import os
import xml.etree.ElementTree as xml

class pdf_parser:
    def __init__(self, given_path, pdf_list):
        self.res_dir = given_path
        self.pdf_list = pdf_list
        self.pdf_res = self.pdf_list.copy()
        self.trees_list = []
        for i, j in enumerate(self.pdf_res):
            self.pdf_res[i] = j.replace('pdf', 'xml')

    def make_xml_from_pdf(self):
        current_path = self.res_dir + '\\members\\'
        target_path = self.res_dir + '\\xml_temp\\'
        for i in range(len(self.pdf_list)):
            current_path += self.pdf_list[i]
            target_path += self.pdf_res[i]
            os.system('pdf2txt.py -o {0} {1}'.format(target_path, current_path))
            current_path = self.res_dir + '\\members\\'
            target_path = self.res_dir + '\\xml_temp\\'
        self.parse_temp_xml()

    def parse_temp_xml(self):
        files_list = os.listdir(path=self.res_dir+'\\xml_temp\\')
        for files in files_list:
            self.make_pdf_trees(files)

    def make_pdf_trees(self, file_to_parse):
        os.chdir(self.res_dir + '\\xml_temp\\')
        tree = xml.parse(file_to_parse)
        self.trees_list.append(tree)
        self.make_pdf_text()

    def make_pdf_text(self):
        os.chdir(self.res_dir + '\\pdf_text_res\\')
        res_f = open('res_pdf.txt', 'w')
        for trees in self.trees_list:
            tr = trees.getroot()
            for i in tr:
                for j in i:
                    for k in j:
                        for h in k:
                            if h.text is None:
                                continue
                            else:
                                res_f.write(h.text)
        res_f.close()

