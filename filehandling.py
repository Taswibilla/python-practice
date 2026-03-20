#csv
import csv
# ----- Write CSV -----
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])   # header
    writer.writerow(["Taswi", 21])     # data
# ----- Read CSV -----
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV Row:", row)
#json
import json
data = {"name": "Taswi", "age": 21}
# ----- Write JSON -----
with open("data.json", "w") as f:
    json.dump(data, f)
# ----- Read JSON -----
with open("data.json", "r") as f:
    data_read = json.load(f)
print("JSON Data:", data_read)
print("Name:", data_read["name"])

#xml
import xml.etree.ElementTree as ET
# ----- Write XML -----
root = ET.Element("person")
ET.SubElement(root, "name").text = "Taswi"
ET.SubElement(root, "age").text = "21"
tree = ET.ElementTree(root)
tree.write("data.xml")
# ----- Read XML -----
tree = ET.parse("data.xml")
root = tree.getroot()
for child in root:
    print("XML Tag:", child.tag, "Value:", child.text)