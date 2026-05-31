from xlrd import *
def read_locators(filename,sheetname):
    workbook=open_workbook(filename)
    sheet=workbook.sheet_by_name(sheetname)
    count=sheet.nrows
    d={}
    for i in range (1,count):
        data=sheet.row_values(i)
        d[data[0]]=[data[1],data[2]]
    return d
def read_data(filename, sheetname):
    workbook=open_workbook(filename)
    sheet=workbook.sheet_by_name(sheetname)
    count=sheet.nrows
    d={}
    for i in range (1,count):
        data=sheet.row_values(i)
        d[data[0]]=data[1]
    return d