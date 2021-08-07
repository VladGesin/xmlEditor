from modules.excelReader import excelReader
from modules.createBCF import createBCF


def main():
    excelData = excelReader()
    createBCF(excelData)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
