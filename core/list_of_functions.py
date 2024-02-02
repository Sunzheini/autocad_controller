from pyautocad import Autocad, APoint
from pyautocad.contrib.tables import Table
import pandas as pd

path = r'C:\Users\User\Desktop\Auto\TBO-G4-02-0.dwg'
excel = r'C:\Users\User\Desktop\Auto\test.xlsx'
text = 'Hello, World!'
list_of_text_objects = []

acad = Autocad(create_if_not_exists=True, visible=True)
document = acad.app.Documents.Open(path)        # acad.app.Documents.Open(path)
print(document)

active_document = acad.doc
document_name = active_document.Name
print(document_name)
acad.prompt(text)

for obj in acad.iter_objects('Text'):
    list_of_text_objects.append(obj)    # will return AcDbText and AcDbMText objects
print([obj.ObjectName for obj in list_of_text_objects])
print([obj.TextString for obj in list_of_text_objects])


def text_contains_3(text_obj):
    return '3' in text_obj.TextString


text_sample = acad.find_one('Text', predicate=text_contains_3)
print(text_sample.TextString)


data = []
for obj in acad.iter_objects('Text'):
    x, y, z = obj.InsertionPoint
    data.append([obj.TextString, x, y, z])

df = pd.DataFrame(data, columns=['Text', 'X', 'Y', 'Z'])
df.to_excel(excel, index=False)


active_document.Save()
active_document.Close()
acad.app.Quit()









