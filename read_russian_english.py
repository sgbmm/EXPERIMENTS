import xml.sax
import os
   
class ExcelHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.chars = [ ]
        self.cells = [ ]
        self.rows = [ ]
        self.tables = [ ]
        
    def characters(self, content):
        self.chars.append(content)
        
    def startElement(self, name, atts):
        if name=="Cell":
            self.chars = [ ]
        elif name=="Row":
            self.cells=[ ]
        elif name=="Table":
            self.rows = [ ]
        
    def endElement(self, name):
        if name=="Cell":
            self.cells.append(''.join(self.chars))
        elif name=="Row":
            self.rows.append(self.cells)
        elif name=="Table":
            self.tables.append(self.rows)
cmd = 'rm -f  output.xml'
os.system(cmd)
cmd = 'wget  "http://search1.ruscorpora.ru/download-xml.xml?mycorp=(lang%3A%22eng%22%20%7C%20lang_trans%3A%22eng%22)&mysent=&mysize=24681277&mysentsize=1608376&text=lexform&mode=para&sort=gr_tagging&env=alpha&req=brother&p=0&dpp=1000&spd=10&spp=1000&out=kwic&dl=xml"  -O output.xml'
os.system(cmd)

excelHandler = ExcelHandler()
xml.sax.parse('output.xml', excelHandler)

# Parsed sheets
excelHandler.tables
for i in range(1,len(excelHandler.tables[0])):
#for ross1 in excelHandler.tables[0]:
  en = excelHandler.tables[0][i][18] 
  en = en[1:en.index('[')]
  ru = excelHandler.tables[0][i][19]
  ru = ru[1:ru.index('[')]
