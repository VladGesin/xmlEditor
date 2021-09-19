import pandas as pd
import os


def excelReader():
    path = os.getcwd()
    data = pd.read_excel(path+'/input.xlsx', sheet_name='CDD')
    ip = pd.read_excel(path+'/input.xlsx', sheet_name='IPRAN')
    data['OAM_IP'] = ip['Unnamed: 4'][2]
    data['IUB_IP'] = ip['Unnamed: 2'][2]
    return data
