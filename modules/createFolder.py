import os


def createFolder(excelData):
    path = os.getcwd()
    if not os.path.exists(path+'/output/'+excelData['SITE'][0]):
        os.mkdir(path+'/output/'+excelData['SITE'][0])