#csv
import csv

# write
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Salary"])
    writer.writerow(["Taswi", 50000])

# read
with open("data.csv", "r") as f:
    for row in csv.reader(f):
        print(row)
#json
import json

data = {"name": "Taswi", "salary": 50000}

# write
with open("data.json", "w") as f:
    json.dump(data, f)

# read
with open("data.json", "r") as f:
    print(json.load(f))
#xml
import xml.etree.ElementTree as ET

# write
root = ET.Element("employee")
name = ET.SubElement(root, "name")
name.text = "Taswi"

ET.ElementTree(root).write("data.xml")

# read
tree = ET.parse("data.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.text)