import xml.etree.ElementTree as ET
import re


def xmlErnc(data, name):
    tree = ET.parse(r"./excelFiles/" + name)
    root = tree.getroot()
    for child in root.iter():
        if child.text:
            value = re.findall(r"(?=(" + '|'.join("%" + data.columns + "%") + r"))", child.text)
            for val in value:
                child.text = child.text.replace(val[0], str(data[val[0].replace("%", "")][0]))
    tree.write("./excelFiles/"+name+"_new.xml", xml_declaration=True, encoding='utf-8')
