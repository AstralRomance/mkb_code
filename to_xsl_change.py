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
            f = open(self.xm_src_dir+xml_file, 'r')
            for i in f:
                templist.append(i)
            self.criteria.append(templist)
            templist = []
        #Формируем список для записи в excel
        for i, headers in enumerate(temp):
            #print(headers)
            finded_info.append(self.get_uniq_code(headers))
            finded_info.append(self.get_mkb_code(headers))
            finded_info.append(self.get_header_text(headers))
            finded_info.append(self.criteria[i])
            self.cells_info.append(finded_info)
            finded_info = []
        #print(self.cells_info)
        #print(self.writing_list)

    def get_mkb_code(self, header):
        temp = ''
        if 'МКБ-10' in header:
            tpl = header.rpartition('МКБ-10')
            temp = tpl[-1]
            temp = temp[2:]
            temp = temp[:-3]
            return(temp)
        else:
            print('ERROR')
            return(None)

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
        return temp

    def create_xls(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Критерии')
        t = 0
        for i, row in enumerate(self.cells_info):
            for j, column in enumerate(self.cells_info[i]):
                ws.write(i, j, self.cells_info[i][j])
                n = j
                for h in self.cells_info[i][3]:
                    print(h)
                    #ws.write(i, n, h)
                    #n += 1

        wb.save(self.dir + '\\res\\criteria.xls')
        print('PARSING IS DONE')