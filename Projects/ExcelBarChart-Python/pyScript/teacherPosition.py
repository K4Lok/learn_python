import requests
import xlsxwriter
from pathlib import Path
#import matplotlib.pyplot as plt

response = requests.get("http://librarydata.library.um.edu.mo/api/TeacherPosition")

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

workbook = xlsxwriter.Workbook('./exportXlsx/teacherPosition.xlsx')
worksheet = workbook.add_worksheet()

headings_format = workbook.add_format()
headings_format.set_bold()
headings_format.set_align('center')

headings = ['Area', 'Count']

worksheet.set_column(0, 0, 25)
worksheet.write_row('A1', headings, headings_format)
worksheet.write_column('A2', areaList)
worksheet.write_column('B2', countList)

myChart = workbook.add_chart({'type': 'pie'})

myChart.set_size({
    'width': 460, 'height': 300
})

#---------------------------All the area--------------
myChart.add_series({
    'name': 'Numbers of Full-time Academic',
    'categories': '=Sheet1!$A$2:$A$8',
    'values':     '=Sheet1!$B$2:$B$8',
})

myChart.set_title ({'name': 'Numbers of Full-time Academic'})

#---------------The title on x,y axis-----------------

#myChart.set_x_axis({'name': 'Number'})
#myChart.set_y_axis({'name': 'Class'})

myChart.set_style(10)

worksheet.insert_chart('D2', myChart)

workbook.close()

print("Done!")