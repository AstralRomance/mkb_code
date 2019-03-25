import os
import xlwt

class xls_parser:
    def __init__(self, maindir):
        self.dir = maindir
        self.pdf_src_dir = maindir + '\\pdf_text_res\\'
        self.xm_src_dir = maindir + '\\res_text\\'
        self.pdf_info = []
        self.criteria = []
        self.cells_info = []

    def make_info(self):
        src_list = os.listdir(self.pdf_src_dir)
        for pdf_file in src_list:
            workf = open(self.pdf_src_dir + pdf_file, 'r')
            for i, j in enumerate(workf):
                if 'Полное название справочника' not in j:
                    self.pdf_info.append(j)
                else:
                    break
            workf.close()
        temp = []
        t = ''
        for i in self.pdf_info:
            while i != ' \n':
                i = i.strip()
                t += i + ' '
                break
            if i == ' \n':
                temp.append(t + ' ')
                t = ''
        finded_info = []
        templist = []
        for xml_file in os.listdir(self.xm_src_dir):
            f = open(self.xm_src_dir+xml_file, 'r', encoding='utf-8')
            for i in f:
                templist.append(i)
            self.criteria.append(templist)
            templist = []
        for i, headers in enumerate(temp):
            finded_info.append(self.get_uniq_code(headers))
            finded_info.append(self.get_mkb_code(headers))
            finded_info.append(self.get_header_text(headers))
            finded_info.append(self.criteria[i])
            self.cells_info.append(finded_info)
            finded_info = []

    def get_mkb_code(self, header):
        temp = ''
        if 'МКБ-10' in header:
            tpl = header.rpartition('МКБ-10')
            temp = tpl[-1]
            temp = temp[2:]
            temp = temp[:-3]
            if ')' in temp:
                temp = temp.replace(')', '')
            if '(' in temp:
                temp = temp.replace('(', '')
            return temp
        elif 'МКБ- 10' in header:
            tpl = header.rpartition('МКБ- 10')
            temp = tpl[-1]
            temp = temp[2:]
            temp = temp[:-3]
            if ')' in temp:
                temp = temp.replace(')', '')
            if '(' in temp:
                temp = temp.replace('(', '')
            return temp
        elif 'MKB-10' in header:
            tpl = header.rpartition('MKB-10')
            temp = tpl[-1]
            temp = temp[2:]
            temp = temp[:-3]
            if ')' in temp:
                temp = temp.replace(')', '')
            if '(' in temp:
                temp = temp.replace('(', '')
            return temp
        else:
            print('ERROR, NO МКБ CODE')
            print(header)
            return None

    def get_uniq_code(self, header):
        temp = ''
        for i in header:
            if i != ' ':
                temp += i
            else:
                break
        return temp

    def get_header_text(self, header):
        temp = ''
        if 'МКБ-10' in header:
            tpl = header.rpartition('МКБ-10')
            temp = tpl[0]
            a = temp.split(' ')
            temp = ''
            i = 1
            while i < len(a)-3:
                temp += a[i] + ' '
                i += 1
            temp = temp.strip()
        elif 'МКБ- 10' in header:
            tpl = header.rpartition('МКБ- 10')
            temp = tpl[0]
            a = temp.split(' ')
            temp = ''
            i = 1
            while i < len(a) - 3:
                temp += a[i] + ' '
                i += 1
            temp = temp.strip()
        elif 'MKB-10' in header:
            tpl = header.rpartition('MKB-10')
            temp = tpl[0]
            a = temp.split(' ')
            temp = ''
            i = 1
            while i < len(a) - 3:
                temp += a[i] + ' '
                i += 1
            temp = temp.strip()
        return temp

    def create_xls(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Критерии', True)
        t = 0
        row_count = 0
        for i, row in enumerate(self.cells_info):
            for j in range(len(self.cells_info[i])-1):
                ws.write(row_count, j, self.cells_info[i][j])
            for k in self.cells_info[i][3]:
                temp = k.split(' ')
                code = temp[0]
                crit_text = ''
                for words in temp[1:]:
                    crit_text += words + ' '
                ws.write(row_count, j+1, code)
                ws.write(row_count, j+2, crit_text)
                row_count += 1
        wb.save(self.dir + '\\res\\res_dict.xls')
