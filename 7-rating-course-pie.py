import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()

# Every JustPy app will have a main object that is known as a Quasar page (Web page)
# JustPy uses the quasar framework built with Javascript that is why it is called as Quasar page

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Rating Per Course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()        # Create a variable (Component) which contains Quasar page instance
    h1=jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")      # Add elements that this page is going to contain. QDiv = Quasar Division
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc_data = [{"name":v1, "y":v2} for v1,v2 in zip(share.index,share)]
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(app)      # justpy is a function and it expects as input a function that returns a quasar page