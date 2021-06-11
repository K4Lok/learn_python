import requests
import xlsxwriter
from pathlib import Path
#import matplotlib.pyplot as plt

response = requests.get("http://librarydata.library.um.edu.mo/api/StuNo")

print(response.status_code)

rsp = response.json()
dataList = []

print(rsp["data"])

for data in rsp["data"]:
    item = [data["years"], data["count"]]
    dataList.append(item)
print(dataList)

def takeYear(elem):
    return elem[0]
dataList.sort(key=takeYear)
print(dataList)

yearList = [2016, 2017, 2018, 2019, 2020]
countList = [[], [], []]

for item in rsp["data"]:
    if(item["title_en"]=="Doctoral"):
        countList[2].append(item["count"])
    elif(item["title_en"]=="Master"):
        countList[1].append(item["count"])
    elif(item["title_en"]=="Bachelor"):
        countList[0].append(item["count"])

print(countList)

# plt.style.use('ggplot')
# plt.barh(print(yearList), countList)
# plt.title("ESI")
# plt.show()

if __name__ == '__main__':
    path_to_folder = Path('../exportXlsx/')
    path_to_folder.mkdir(exist_ok=True)
    workbook = xlsxwriter.Workbook('../exportXlsx/StuNo.xlsx')
else:
    path_to_folder = Path('./exportXlsx/')
    path_to_folder.mkdir(exist_ok=True)
    workbook = xlsxwriter.Workbook('./exportXlsx/StuNo.xlsx')




worksheet = workbook.add_worksheet()

headings_format = workbook.add_format()
headings_format.set_bold()
headings_format.set_align('center')

headings = ['Bachelor', 'Master', 'Doctoral']

worksheet.write_row('B1', headings, headings_format)
worksheet.write_column('A2', yearList)
worksheet.write_column('B2', countList[0])
worksheet.write_column('C2', countList[1])
worksheet.write_column('D2', countList[2])


myChart = workbook.add_chart({'type': 'column'})

#---------------------------2016-------------------------------
myChart.add_series({
    'name': '2016',
    'categories': '=Sheet1!$D$1:$B$1',
    'values':     '=Sheet1!$D$2:$B2',
    'fill':       {'color': '#23F598'},
    'line':       {'color': '#FFFFFF', 'width': 1},
})

#---------------------------2017-------------------------------
myChart.add_series({
    'name': '2017',
    'categories': '=Sheet1!$D$1:$B$1',
    'values':     '=Sheet1!$D$3:$B$3',
    'fill':       {'color': '#23B3F5'},
    'line':       {'color': '#FFFFFF', 'width': 1},
})

#---------------------------2018-------------------------------
myChart.add_series({
    'name': '2018',
    'categories': '=Sheet1!$D$1:$B$1',
    'values':     '=Sheet1!$D$4:$B$4',
    'fill':       {'color': '#F56969'},
    'line':       {'color': '#FFFFFF', 'width': 1},
})

#---------------------------2019-------------------------------
myChart.add_series({
    'name': '2019',
    'categories': '=Sheet1!$D$1:$B$1',
    'values':     '=Sheet1!$D$5:$B$5',
    'fill':       {'color': '#F79B36'},
    'line':       {'color': '#FFFFFF', 'width': 1},
})

#---------------------------2020-------------------------------
myChart.add_series({
    'name': '2020',
    'categories': '=Sheet1!$D$1:$B$1',
    'values':     '=Sheet1!$D$6:$B$6',
    'fill':       {'color': '#0E6F9B'},
    'line':       {'color': '#FFFFFF', 'width': 1},
})

myChart.set_title ({'name': 'Student Quantities'})

#---------------The title on x,y axis-----------------

#myChart.set_x_axis({'name': 'Number'})
#myChart.set_y_axis({'name': 'Class'})

#myChart.set_style(12)

worksheet.insert_chart('F2', myChart)

workbook.close()

print("Done!")