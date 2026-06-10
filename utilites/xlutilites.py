from xlrd import *
import os

def _resolve_path(filename):
    if os.path.isabs(filename):
        return filename
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.normpath(os.path.join(base, filename))


def read_locators(filename,sheetname):
    filename = _resolve_path(filename)
    workbook=open_workbook(filename)
    sheet=workbook.sheet_by_name(sheetname)
    count=sheet.nrows
    d={}
    for i in range (1,count):
        data=sheet.row_values(i)
        d[data[0]]=[data[1],data[2]]
    return d
def read_data(filename, sheetname):
    filename = _resolve_path(filename)
    workbook=open_workbook(filename)
    sheet=workbook.sheet_by_name(sheetname)
    count=sheet.nrows
    d={}
    for i in range (1,count):
        data=sheet.row_values(i)
        d[data[0]]=data[1]
    return d