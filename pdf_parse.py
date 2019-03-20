import os
import xml.etree.ElementTree as xml


class pdf_parser:
    def __init__(self, given_path, pdf_list):
        self.res_dir = given_path
        self.pdf_list = pdf_list
        self.trees_list = []

    def make_xml_from_pdf(self):
        current_path = self.res_dir + '\\members\\'
        target_path = self.res_dir + '\\xml_temp\\'
        for i in self.pdf_list:
            temp = i.split('\\')
            file_to_copy = temp[-1][:-3] + 'xml'
            file_to_copy = target_path + file_to_copy
            os.system('pdf2txt.py -o {0} {1}'.format(file_to_copy, i))
        self.make_pdf_text(file_to_copy)

    def make_pdf_text(self, filename):
        os.chdir(self.res_dir + '\\xml_temp\\')
        xml_list = os.listdir(self.res_dir + '\\xml_temp\\')
        for cfile in xml_list:
            tree = xml.parse(cfile)
            temp = cfile.split('\\')
            fname = temp[-1][:-3]
            res_f = open(self.res_dir + '\\pdf_text_res\\' + fname + 'txt', 'w')
            tr = tree.getroot()
            for i in tr:
                for j in i:
                    for k in j:
                        for h in k:
                            if h.text is None:
                                continue
                            else:
                                res_f.write(h.text)


        res_f.close()
