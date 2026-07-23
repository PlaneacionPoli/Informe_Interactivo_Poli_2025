import zipfile, re, xml.etree.ElementTree as ET
path = r"data\indicadores\CMI Estrategico.xlsx"
z = zipfile.ZipFile(path)
wb_xml = z.read("xl/workbook.xml").decode("utf-8")
matches = re.findall(r'<sheet\b[^>]*\bname="([^"]*)"', wb_xml)
print("Sheets:", matches)
ss = []
try:
    ss_xml = z.read("xl/sharedStrings.xml").decode("utf-8")
    ss = [t.text or "" for t in ET.fromstring(ss_xml).iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
except KeyError:
    pass
sh_xml = z.read("xl/worksheets/sheet1.xml").decode("utf-8")
root = ET.fromstring(sh_xml)
rows = []
for row in root.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row"):
    cells = {}
    for c in row.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c"):
        ref = c.get("r")
        t = c.get("t")
        v = c.find("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v")
        if v is not None:
            val = v.text
            if t == "s":
                val = ss[int(val)]
            cells["".join(ch for ch in ref if ch.isalpha())] = val
    rows.append(cells)
print("Header letters:", list(rows[0].keys()))
print("Header values:", [rows[0][k] for k in sorted(rows[0].keys())])
