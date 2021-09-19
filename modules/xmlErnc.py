import xml.etree.ElementTree as ET
import re
import os


def xmlErnc(data, name):
    path = os.getcwd()
    tree = ET.parse(path+"/excelFiles/" + name)
    root = tree.getroot()
    for child in root.iter():
        if child.text:
            value = re.findall(r"(?=(" + '|'.join("%" + data.columns + "%") + r"))", child.text)
            for val in value:
                child.text = child.text.replace(val[0], str(data[val[0].replace("%", "")][0]))
    tree.write(path+'/output/'+data['SITE'][0]+"/"+data['SITE'][0]+'_'+data['RNC'][0]+'.xml', xml_declaration=True, encoding='utf-8')
