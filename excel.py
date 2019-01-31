from openpyxl import Workbook
from openpyxl.packaging.core import DocumentProperties
from openpyxl.packaging.manifest import Manifest, Override
from openpyxl.packaging.workbook import WorkbookParser
from openpyxl.packaging.relationship import get_dependents, get_rels_path

from openpyxl.worksheet.read_only import ReadOnlyWorksheet
from openpyxl.worksheet.table import Table
from openpyxl.drawing.spreadsheet_drawing import SpreadsheetDrawing
from openpyxl.chart.reader import find_charts

from openpyxl.xml.functions import fromstring
from xlrd import open_workbook

import openpyxl

import pandas as pd

# file = 'Kopya_ANKARA_BILGI_PORTALI-GUNCEL.XLSX'
#
# xl = pd.ExcelFile(file)
# print(xl.sheet1)
# df1 = xl.parse('Sheet1')

fList = []
cList = []
kelime_list = "ABCDEFG"
wb = openpyxl.load_workbook('Kopya_ANKARA_BILGI_PORTALI-GUNCEL.xlsx')

sheet = wb.get_sheet_by_name('Sayfa1')

sheet = wb.active


for i in sheet['C']:
    cList.append(str(i.value))

print (cList)

# cell = sheet['D5'].value
# print (cell)


# #print (cList)
# for line in range(1,1062,1):
#
#         line_value = {"BOLUM_ADI": sheet['A'+str(line)].value, "DOKTORLAR": sheet['B'+str(line)].value, "TAKIP_EDILEN_HASTALIKLAR": sheet['C'+str(line)].value, "NOT": sheet['D'+str(line)].value, "RANDEVU_PLANLAMA": sheet['E'+str(line)].value, "KONTROL_SURELERI": sheet['F'+str(line)].value, "MUAYENE_UCRETI(CARI)": sheet['G'+str(line)].value }
#         fList.append(line_value)
#         print (line_value)
