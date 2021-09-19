import xml.etree.ElementTree as ET
import re
import os


def createBCF(data):
    path = os.getcwd()
    tree = ET.parse(path+"/excelFiles/BCF_TEMPLATE.xml")
    rootBatch = tree.find('Batch')
    rootBatch.set('batchName', data['SITE'][0] + "_IPSEC")

    for neighbor in rootBatch.iter('SubstitutionAttribute'):
        value = re.findall(r"(?=(" + '|'.join("%" + data.columns + "%") + r"))", neighbor.attrib['value'])
        for val in value:
            neighbor.set('value', neighbor.attrib['value'].replace(val[0], str(data[val[0].replace("%", "")][0])))

    tree.write(path+'/output/'+data['SITE'][0]+"/"+data['SITE'][0]+'_BCF.xml', xml_declaration=True, encoding='utf-8')
