from django.shortcuts import render

from trips.models import Post

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts
from collections import OrderedDict


#首頁
def home(request):
  post_list = Post.objects.all()
  TaiwanChart(request)
  return render(request, 'home.html', {'post_list': post_list})


def TaiwanChart(request):
  # Reference: https://www.fusioncharts.com/dev/api/fusioncharts/fusioncharts-events#dataplotclick-261
  # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  # The data is passed as a string in the `dataSource` as parameter.
  dataSource = OrderedDict()

  # The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  chartConfig["caption"] = "The Administrative Region of Taiwan"
  chartConfig["subcaption"] = "SIRLA 2020-07"
  chartConfig["showLabels"] = "0"
  chartConfig["numberSuffix"] = "°C"
  chartConfig["borderThickness"] = "0.5"
  chartConfig["theme"] = "fusion" # fusion, gammel, candy, umber
  chartConfig["entityToolText"] = "<b>$lname</b> has an average temperature of <b>$datavalue</b>"
  dataSource["chart"] = chartConfig

  colorrange_chartConfig = OrderedDict()
  colorrange_chartConfig["minvalue"] = "20"
  colorrange_chartConfig["code"] = "#00A971"
  colorrange_chartConfig["gradient"] = "1"
  colorrange_chartConfig["color"] = []
  colorrange_chartConfig["color"].append({"minvalue": '10', "maxvalue": '30', "code": '#EFD951'})
  colorrange_chartConfig["color"].append({"minvalue": '30', "maxvalue": '50', "code": '#FD8963'})
  colorrange_chartConfig["color"].append({"minvalue": '50', "maxvalue": '80', "code": '#D60100'})
  dataSource["colorrange"] = colorrange_chartConfig

  dataSource["data"] = []
  # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
  # Insert the data into the `dataSource['data']` list.
  dataSource["data"].append({"ID": "01", "Label": "Changhua County", "value": "70.0", "link": ""})
  dataSource["data"].append({"ID": "02", "Label": "Chiayi County", "value": "52.3", "link": ""})
  dataSource["data"].append({"ID": "03", "Label": "Chiayi City", "value": "54.2", "link": ""})
  dataSource["data"].append({"ID": "04", "Label": "Hsinchu County", "value": "55.3", "link": ""})
  dataSource["data"].append({"ID": "05", "Label": "Hsinchu City", "value": "50.1", "link": ""})
  dataSource["data"].append({"ID": "06", "Label": "Hualien County", "value": "28.5", "link": ""})
  dataSource["data"].append({"ID": "09", "Label": "Keelung City", "value": "29.3", "link": ""})
  dataSource["data"].append({"ID": "10", "Label": "Kinmen County", "value": "59.4", "link": ""})
  dataSource["data"].append({"ID": "11", "Label": "Lienchiang County", "value": "26.6", "link": ""})
  dataSource["data"].append({"ID": "12", "Label": "Miaoli County", "value": "44.4", "link": ""})
  dataSource["data"].append({"ID": "13", "Label": "Nantou County", "value": "49.9", "link": ""})
  dataSource["data"].append({"ID": "14", "Label": "Penghu County", "value": "28.7", "link": ""})
  dataSource["data"].append({"ID": "15", "Label": "Pingtung County", "value": "42.7", "link": ""})
  dataSource["data"].append({"ID": "20", "Label": "New Taipei City", "value": "32.0", "link": "https://www.cwb.gov.tw/V8/C/"})
  dataSource["data"].append({"ID": "21", "Label": "Taipei City", "value": "29.6", "link": ""})
  dataSource["data"].append({"ID": "22", "Label": "Taitung County", "value": "28.9", "link": ""})
  dataSource["data"].append({"ID": "23", "Label": "Taoyuan City", "value": "32.0", "link": ""})
  dataSource["data"].append({"ID": "24", "Label": "Yilan County", "value": "28.6", "link": ""})
  dataSource["data"].append({"ID": "25", "Label": "Yunlin County", "value": "45.2", "link": ""})
  dataSource["data"].append({"ID": "26", "Label": "Taichung City", "value": "28.6", "link": ""})
  dataSource["data"].append({"ID": "27", "Label": "Kaohsiung City", "value": "29.2", "link": ""})
  dataSource["data"].append({"ID": "28", "Label": "Tainan City", "value": "29.2", "link": ""})

  # Create an object for the map using the FusionCharts class constructor 
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/taiwan", "TaiwanChart", "950", "750", "TaiwanChart-container", "json", dataSource)
  # returning complete JavaScript and HTML code, which is used to generate map in the browsers. 
  return render(request, 'home.html', {'output': fusionMap.render(), 'chartTitle': 'Taiwan Map'})