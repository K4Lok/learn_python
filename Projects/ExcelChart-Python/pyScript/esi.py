import requests
import xlsxwriter
from pathlib import Path
#import matplotlib.pyplot as plt


response = requests.get("http://librarydata.library.um.edu.mo/api/esi")

print(response.status_code)

rsp = response.json()
dataList = []

print(rsp["data"])

for data in rsp["data"]:
    item = [data["name"], data["name_en"], data["count"]]
    dataList.append(item)
print(dataList)

def takeThird(elem):
    return elem[2]
dataList.sort(key=takeThird)
print(dataList)

nameList = []
nameEnList = []
countList = []

for item in dataList:
    nameList.append(item[0])
    nameEnList.append(item[1])
    countList.append(item[2])

print(nameList)
print(nameEnList)
print(countList)

# plt.style.use('ggplot')
# plt.barh(nameEnList, countList)
# plt.title("ESI")
# plt.show()

path_to_folder = Path('./exportXlsx/')
path_to_folder.mkdir(exist_ok=True)

workbook = xlsxwriter.Workbook('./exportXlsx/esi.xlsx')
worksheet = workbook.add_worksheet()

headings_format = workbook.add_format()
headings_format.set_bold()
headings_format.set_align('center')

headings = ['Name', 'Name_en', 'Count']

worksheet.set_column(0, 1, 25)
worksheet.write_row('A1', headings, headings_format)
worksheet.write_column('A2', nameList)
worksheet.write_column('B2', nameEnList)
worksheet.write_column('C2', countList)

myChart = workbook.add_chart({'type': 'bar', 'subtype': 'stacked'})

myChart.add_series({
    'name':       '=Sheet1!$C$1',
    'categories': '=Sheet1!$A$2:$A$11',
    'values':     '=Sheet1!$C$2:$C$11',
    'fill':       {'color': '#2D8479'},
    'border':       {'color': '#2D8479', 'width': 1.25},
})

myChart.set_title ({'name': 'ESI'})

#---------------The title on x,y axis-----------------

#myChart.set_x_axis({'name': 'Number'})
#myChart.set_y_axis({'name': 'Class'})

myChart.set_style(12)

worksheet.insert_chart('E2', myChart)

workbook.close()

print("Done!")