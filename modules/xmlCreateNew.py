import xml.etree.ElementTree as ET
import re


def xmlCreation(data):
    tree = ET.parse("./excelFiles/ERNC2_ICF_TEMPLATE.xml")
    ET.register_namespace("", "http://www.w3.org/2001")
    root = tree.getroot()
    for child in root.iter():
        if child.text:
            value = re.findall(r"(?=(" + '|'.join("%" + data.columns + "%") + r"))", child.text)
            for val in value:
                child.text = child.text.replace(val[0], str(data[val[0].replace("%", "")][0]))
    ET.register_namespace("", "/excelFiles/ERNC2_ICF_TEMPLATE.xml")
    tree.write("./excelFiles/ERNC2_ICF_TEMPLATE_new.xml")
