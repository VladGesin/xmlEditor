from modules.excelReader import excelReader
from modules.createBCF import createBCF
from modules.xmlErnc import xmlErnc


def main():
    excelData = excelReader()
    createBCF(excelData)
    xmlErnc(excelData, 'ERNC1_ICF_TEMPLATE.xml')
    xmlErnc(excelData, 'ERNC2_ICF_TEMPLATE.xml')


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
