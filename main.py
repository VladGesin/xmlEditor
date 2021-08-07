from modules.excelReader import excelReader
from modules.createBCF import createBCF
from modules.xmlCreateNew import xmlCreation

def main():
    excelData = excelReader()
    # createBCF(excelData)
    xmlCreation(excelData)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
