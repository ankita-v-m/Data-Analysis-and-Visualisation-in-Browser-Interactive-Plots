import justpy as jp
from pandas.core.dtypes.common import classes

import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

# Every JustPy app will have a main object that is known as a Quasar page (Web page)
# JustPy uses the quasar framework built with Javascript that is why it is called as Quasar page

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range:1990 to 2050'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 1 to 10'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()        # Create a variable (Component) which contains Quasar page instance
    h1=jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")      # Add elements that this page is going to contain. QDiv = Quasar Division
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc=jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Week"
    
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])

    return wp

jp.justpy(app)      # justpy is a function and it expects as input a function that returns a quasar page