import requests
import xlsxwriter
from pathlib import Path
#import matplotlib.pyplot as plt

response = requests.get("http://librarydata.library.um.edu.mo/api/citationimpact")

print(response.status_code)

rsp = response.json()
dataList = []

print(rsp["data"])

for data in rsp["data"]:
    item = [data["year"], data["count"]]
    dataList.append(item)
print(dataList)

def takeYear(elem):
    return elem[0]
dataList.sort(key=takeYear)
print(dataList)

yearList = []
countList = []

for item in dataList:
    yearList.append(item[0])
    countList.append(item[1])

print(yearList)
print(countList)

path_to_folder = Path('./exportXlsx/')
path_to_folder.mkdir(exist_ok=True)

workbook = xlsxwriter.Workbook('./exportXlsx/citationImpact.xlsx')
worksheet = workbook.add_worksheet()

headings_format = workbook.add_format()
headings_format.set_bold()
headings_format.set_align('center')

headings = ['Year', 'Count']

worksheet.write_row('A1', headings, headings_format)
worksheet.write_column('A2', yearList)
worksheet.write_column('B2', countList)

myChart = workbook.add_chart({'type': 'line', 'subtype': 'stacked'})

myChart.add_series({
    'name': '',
    'categories': '=Sheet1!$A$2:$A$12',
    'values':     '=Sheet1!$B$2:$B$12',
    'line':       {'color': '#2D8479', 'width': 1.5},
    'marker': {'type': 'square',
               'size,': 10,
               'border': {'color': '#2D8479'},
               'fill':   {'color': '#FFFFFF'}
    },
    'data_labels': {
        'value': True , 'position': 'above',
        'font': {'name': 'Consolas', 'color': '#2D8479'}
        },
})

myChart.set_legend({'none': True})

myChart.set_title ({'name': 'Citation Impact'})

#---------------The title on x,y axis-----------------

#myChart.set_x_axis({'name': 'Number'})
#myChart.set_y_axis({'name': 'Class'})

myChart.set_style(12)

worksheet.insert_chart('E2', myChart)

workbook.close()

print("Done!")