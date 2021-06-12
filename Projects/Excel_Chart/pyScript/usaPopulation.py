import requests
import xlsxwriter
from pathlib import Path
#import matplotlib.pyplot as plt

response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

print(response.status_code)

rsp = response.json()
dataList = []

print(rsp["data"])

for data in rsp["data"]:
    item = [data["Nation"], data["Year"], data["Population"]]
    dataList.append(item)
print(dataList)

def takeYear(elem):
    return elem[1]
dataList.sort(key=takeYear)
print(dataList)

nationList = []
yearList = []
popuList = []

INDEX_NATION = 0
INDEX_YEAR = 1
INDEX_POPULATION = 2

for item in dataList:
    nationList.append(item[INDEX_NATION])
    yearList.append(item[INDEX_YEAR])
    popuList.append(item[INDEX_POPULATION])

print(yearList)
print(popuList)

path_to_folder = Path('./xlsxExport/')
path_to_folder.mkdir(exist_ok=True)

workbook = xlsxwriter.Workbook('./xlsxExport/usaPopulation.xlsx')
worksheet = workbook.add_worksheet()

headings_format = workbook.add_format()
headings_format.set_bold()
headings_format.set_align('center')

headings = ['Nation', 'Year', 'Population']

worksheet.set_column(0, 0, 14)
worksheet.set_column(1, 1, 8)
worksheet.set_column(2, 2, 15)

worksheet.write_row('A1', headings, headings_format)
worksheet.write_column('A2', nationList)
worksheet.write_column('B2', yearList)
worksheet.write_column('C2', popuList)

myChart = workbook.add_chart({'type': 'column'})

myChart.set_size({
    'width': 560, 'height': 300
})

# myChart.set_legend({
#     'font': {'size': 9},
#         'layout': {
#         'x':      0.80,
#         'y':      0.37,
#         'width':  22,
#         'height': 25,
#     }
# })

#---------------------------All the area--------------
myChart.add_series({
    'name': 'USA Population',
    'categories': '=Sheet1!$B$2:$B$7',
    'values':     '=Sheet1!$C$2:$C$7'
})

myChart.set_title ({'name': 'USA Population'})

#---------------The title on x,y axis-----------------

#myChart.set_x_axis({'name': 'Number'})
#myChart.set_y_axis({'name': 'Class'})

myChart.set_style(10)

worksheet.insert_chart('E2', myChart)

workbook.close()

print("Done!")