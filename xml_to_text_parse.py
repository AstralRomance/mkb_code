import xml.etree.ElementTree as xml
import os

class xml_parse:
    def __init__(self, given_path, xml_list):
        self.mem_list = xml_list
        self.res_dir = given_path + '\\res_text'
        self.trees_list = []
        self.id_list = []
        self.name_list = []
        try:
            os.mkdir(self.res_dir)
        except OSError:
            pass

    def get_file_list(self):
        for files in self.mem_list:
            self.get_xml_info(files)

    def get_xml_info(self, xml_input):
        tree = xml.parse(xml_input)
        self.trees_list.append(tree)
        for roots in self.trees_list:
            roots = roots.getroot()

    def xml_to_text(self):
        os.chdir(self.res_dir)
        res_f = open('res_text.txt', 'w')
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

