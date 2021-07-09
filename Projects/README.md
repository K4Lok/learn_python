Python version: 3.6.x

Library required: requests, xlsxwriter, pathlib

Library installation:
    pip install requests   || pip3 install requests
    pip install xlsxwriter || pip3 install xlsxwriter
    pip install pathlib    || pip3 install pathlib

Check whether the library installed properly:
    pip list || pip3 list

What the script does:
    Requests GET API
    Get the json data
    Put it into excel file
    Genarate the Charts

API website:
    USA Population     : "https://datausa.io/api/data?drilldowns=Nation&measures=Population"             

More infos:
    HTTP Requests      : "https://docs.python-requests.org/en/master/"
    Directory exits    : "https://docs.python.org/3/library/pathlib.html", Path.mkdir(mode=0o777, parents=False, exist_ok=False)
    Xlsx Chart Style   : "https://xlsxwriter.readthedocs.io/working_with_charts.html#chart-layout"
    Bar Chart          : "https://xlsxwriter.readthedocs.io/example_chart_bar.html?highlight=bar%20chart"
    Column Chart       : "https://xlsxwriter.readthedocs.io/example_chart_column.html?highlight=column%20chart"
    Doughunt Chart     : "https://xlsxwriter.readthedocs.io/example_chart_doughnut.html"
    Doughunt Set Hole  : "https://xlsxwriter.readthedocs.io/chart.html?highlight=Doughnut%20Chart#set_hole_size"
    Pie Chart          : "https://xlsxwriter.readthedocs.io/example_chart_pie.html?highlight=pie%20chart"
    Adjust Cell Width  : "https://stackoverflow.com/questions/33665865/adjust-cell-width-in-excel/33665967"
    Exec other .py     : "https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script"
