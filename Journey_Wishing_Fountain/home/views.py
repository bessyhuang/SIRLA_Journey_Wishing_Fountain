from django.shortcuts import render

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts
from collections import OrderedDict

# Loading Data from a Ordered Dictionary
# Example to create a Map with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.

def chart(request):
  # Reference: https://www.fusioncharts.com/dev/api/fusioncharts/fusioncharts-events#dataplotclick-261
  # Create an object for the map using the FusionCharts class constructor  
  # The chart data is passed to the `dataSource` parameter.
  fusionMap = FusionCharts("maps/taiwan", "ex1" , "650", "450", "chart-1", "json",
          # The data is passed as a string in the `dataSource` as parameter.
    	
    	#"theme": "fusion",  
    	# fusion, gammel, candy, umber
		
    """{
	    "chart": {
	      "caption": "The Administrative Region of Taiwan",
	      "subcaption": "SIRLA 2020",
	      "showLabels": "0",
	      "numberSuffix": "°C",
	      "borderThickness": "0.5",
	      "theme": "fusion",
	      "entityToolText": "<b>$lname</b> has an average temperature of <b>$datavalue</b>"
	    },
      "colorrange": {
        "minvalue": "20",
        "code": "#00A971",
        "gradient": "1",
        "color": [{
            "minvalue": "20",
            "maxvalue": "40",
            "code": "#EFD951"
          }, {
            "minvalue": "40",
            "maxvalue": "60",
            "code": "#FD8963"
          },
          {
            "minvalue": "60",
            "maxvalue": "80",
            "code": "#D60100"
          }

        ]
      },
      "data": [{
      	  "ID": "01",
          "Label": "Changhua County",
          "value": "70.0",
          "link": ""
        },
        {
      	  "ID": "02",
          "Label": "Chiayi County",
          "value": "52.3",
          "link": ""
        },
        {
          "ID": "03",
          "Label": "Chiayi City",
          "value": "54.2",
          "link": ""
        },
        {
          "ID": "04",
          "Label": "Hsinchu County",
          "value": "55.3",
          "link": ""
        },
        {
          "ID": "05",
          "Label": "Hsinchu City",
          "value": "50.1",
          "link": ""
        },
        {
          "ID": "06",
          "Label": "Hualien County",
          "value": "48.3",
          "link": ""
        },
        {
          "ID": "09",
          "Label": "Keelung City",
          "value": "32.0",
          "link": ""
        },
        {
          "ID": "10",
          "Label": "Kinmen County",
          "value": "59.4",
          "link": ""
        },
        {
          "ID": "11",
          "Label": "Lienchiang County",
          "value": "26.6",
          "link": ""
        },
        {
          "ID": "12",
          "Label": "Miaoli County",
          "value": "44.4",
          "link": ""
        },
        {
          "ID": "13",
          "Label": "Nantou County",
          "value": "49.9",
          "link": ""
        },
        {
          "ID": "14",
          "Label": "Penghu County",
          "value": "60.3",
          "link": ""
        },
        {
          "ID": "15",
          "Label": "Pingtung County",
          "value": "42.7",
          "link": ""
        },
        {
          "ID": "20",
          "Label": "New Taipei City",
          "value": "32.0",
          "link": "https://www.cwb.gov.tw/V8/C/"
        },
        {
          "ID": "21",
          "Label": "Taipei City",
          "value": "32.0",
          "link": ""
        },
        {
          "ID": "22",
          "Label": "Taitung County",
          "value": "45.1",
          "link": ""
        },
        {
          "ID": "23",
          "Label": "Taoyuan City",
          "value": "32.0",
          "link": ""
        },
        {
          "ID": "24",
          "Label": "Yilan County",
          "value": "40.4",
          "link": ""
        },
        {
          "ID": "25",
          "Label": "Yunlin County",
          "value": "45.2",
          "link": ""
        },
        {
          "ID": "26",
          "Label": "Taichung City",
          "value": "48.8",
          "link": ""
        },
        {
          "ID": "27",
          "Label": "Kaohsiung City",
          "value": "54.3",
          "link": ""
        },
        {
          "ID": "28",
          "Label": "Tainan City",
          "value": "59.6",
          "link": ""
        }
      ]
      }""")

  # returning complete JavaScript and HTML code, which is used to generate map in the browsers. 
  return  render(request, 'index.html', {'output' : fusionMap.render(), 'chartTitle': 'Taiwan Map'})
