import xml.etree.ElementTree as ET
import re


def createBCF(data):
    tree = ET.parse("./excelFiles/BCF_TEMPLATE.xml")
    rootBatch = tree.find('Batch')
    rootBatch.set('batchName', data['SITE'][0] + "_IPSEC")

    for neighbor in rootBatch.iter('SubstitutionAttribute'):
        value = re.findall(r"(?=(" + '|'.join("%" + data.columns + "%") + r"))", neighbor.attrib['value'])
        for val in value:
            neighbor.set('value', neighbor.attrib['value'].replace(val[0], str(data[val[0].replace("%", "")][0])))

    tree.write("./excelFiles/BCF_TEMPLATE_new.xml")
