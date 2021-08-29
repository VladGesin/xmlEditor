from modules.excelReader import excelReader
from modules.createBCF import createBCF
from modules.xmlErnc import xmlErnc
from modules.createFolder import createFolder

def main():
    excelData = excelReader()
    createFolder(excelData)
    createBCF(excelData)
    if excelData['RNC'][0]=='RNC1':
        xmlErnc(excelData, 'ERNC1_ICF_TEMPLATE.xml')
    else:
        xmlErnc(excelData, 'ERNC2_ICF_TEMPLATE.xml')


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
