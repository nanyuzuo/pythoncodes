import os
import shutil
import openpyxl

def searchZone(name):
    wb = openpyxl.load_workbook("/Users/Wendy/学生地区.xlsx")
    sheet = wb["地区表"]
    for row in sheet.rows:
        if row[0].value == name:
            return row[1].value

path = "/Users/Wendy/学生资料"
allItems = os.listdir(path)
for item in allItems:
    filePath = os.path.join(path,item)
    name = os.path.splitext(item)[0]
    zone = searchZone(name)
    targetPath = os.path.join(path,zone)
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)
    shutil.move(filePath,targetPath)