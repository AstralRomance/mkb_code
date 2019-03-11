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
        self.parse_temp_xml()

    def parse_temp_xml(self):
        files_list = os.listdir(path=self.res_dir+'\\xml_temp\\')
        print('files list')
        print(files_list)
        for files in files_list:
            self.make_mkb_text(files)

    def make_mkb_text(self, file_to_parse):
        print(file_to_parse)
        curr_dir = self.res_dir + '\\xml_temp\\' + file_to_parse
        tree = xml.parse(curr_dir)
        self.trees_list.append(tree)
        for roots in self.trees_list:
            roots = roots.getroot()

    def make_text_from_pdf(self):
        os.chdir(self.res_dir)
        res_f = open('res_text_from_pdf.txt', 'w')
        for trees in self.trees_list:
            tr = trees.getroot()
            for i in tr:
                for j in i:
                    for k in j:
                        k.text = k.text[0::] + ' '
                        l = k.text.split('\r')
                        while 'Да/Нет' in l:
                            l.remove('Да/Нет')
                        while '\r\n' in l:
                            l.remove('\r\n')
                        for strs in l:
                            if strs == ' ':
                                continue
                            else:
                                res_f.write(strs)
                    res_f.write('\r')
                res_f.write('\r')
