import pandas as pd


def excelReader():
    data = pd.read_excel('./excelFiles/CDD for UMPIC82 Ericsson Faten -birzeit.xlsx', sheet_name='CDD')
    ip = pd.read_excel('./excelFiles/CDD for UMPIC82 Ericsson Faten -birzeit.xlsx', sheet_name='IPRAN')
    data['OAM_IP'] = ip['Unnamed: 4'][2]
    data['IUB_IP'] = ip['Unnamed: 2'][2]
    return data