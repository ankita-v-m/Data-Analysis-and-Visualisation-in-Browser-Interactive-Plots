import justpy as jp
from pandas.core.dtypes.common import classes

import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month','Course Name'])['Rating'].count().unstack()

# Every JustPy app will have a main object that is known as a Quasar page (Web page)
# JustPy uses the quasar framework built with Javascript that is why it is called as Quasar page

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Course by month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp = jp.QuasarPage()        # Create a variable (Component) which contains Quasar page instance
    h1=jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")      # Add elements that this page is going to contain. QDiv = Quasar Division
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc=jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Course by Month"
    
    hc.options.xAxis.categories = list(month_average_crs.index)

    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]

    hc.options.series = hc_data

    return wp

jp.justpy(app)      # justpy is a function and it expects as input a function that returns a quasar page