from xlrd import *
import os

def _resolve_path(filename):
    if os.path.isabs(filename):
        return filename

    root = os.path.dirname(os.path.dirname(__file__))
    candidate = os.path.normpath(os.path.join(root, filename))
    if os.path.exists(candidate):
        return candidate

    normalized = os.path.normpath(filename)
    while normalized.startswith('..' + os.sep):
        normalized = normalized[len('..' + os.sep):]
    normalized = normalized.lstrip(os.sep)
    return os.path.normpath(os.path.join(root, normalized))


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