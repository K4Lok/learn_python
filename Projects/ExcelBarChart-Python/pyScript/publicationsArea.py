import requests
import xlsxwriter
from pathlib import Path
#import matplotlib.pyplot as plt

response = requests.get("http://librarydata.library.um.edu.mo/api/PublicationsArea")

print(response.status_code)

rsp = response.json()
dataList = []

print(rsp["data"])

for data in rsp["data"]:
    item = [data["title_en"], data["count"]]
    dataList.append(item)
print(dataList)

def takeCount(elem):
    return elem[1]
dataList.sort(key=takeCount)
print(dataList)

areaList = []
countList = []

for item in rsp["data"]:
    areaList.append(item['title_en'])
    countList.append(item['count'])

print(countList)

path_to_folder = Path('./exportXlsx/')
path_to_folder.mkdir(exist_ok=True)

workbook = xlsxwriter.Workbook('./exportXlsx/publicationsArea.xlsx')
worksheet = workbook.add_worksheet()

headings_format = workbook.add_format()
headings_format.set_bold()
headings_format.set_align('center')

headings = ['Area', 'Count']

worksheet.set_column(0, 0, 40)
worksheet.write_row('A1', headings, headings_format)
worksheet.write_column('A2', areaList)
worksheet.write_column('B2', countList)

myChart = workbook.add_chart({'type': 'doughnut'})

myChart.set_hole_size(70)

myChart.set_size({
    'width': 660, 'height': 600
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
    'name': 'Publications by Subject Area',
    'categories': '=Sheet1!$A$2:$A$14',
    'values':     '=Sheet1!$B$2:$B$14',
})

myChart.set_title ({'name': 'Publications by Subject Area'})

#---------------The title on x,y axis-----------------

#myChart.set_x_axis({'name': 'Number'})
#myChart.set_y_axis({'name': 'Class'})

myChart.set_style(10)

worksheet.insert_chart('D2', myChart)

workbook.close()

print("Done!")