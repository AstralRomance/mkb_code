import xml.etree.ElementTree as xml
import os

class xml_parse:
    def __init__(self, given_path, xml_list):
        self.mem_list = xml_list
        self.res_dir = given_path
        self.trees_list = []
        self.id_list = []
        self.name_list = []
        try:
            os.mkdir(self.res_dir+'\\res_text')
        except OSError:
            pass

    def xml_to_text_parse(self):
        os.chdir(self.res_dir + '\\res_text\\')
        for cfile in self.mem_list:
            tree = xml.parse(cfile)
            temp = cfile.split('\\')
            filename = temp[-1]
            filename = filename[:-3]
            res_f = open(filename + 'txt', 'w', encoding='utf-8')
            tr = tree.getroot()
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
                    res_f.write('\n')
            res_f.close()
