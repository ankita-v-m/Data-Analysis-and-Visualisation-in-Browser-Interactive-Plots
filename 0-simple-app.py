import justpy as jp
from pandas.core.dtypes.common import classes

# Every JustPy app will have a main object that is known as a Quasar page (Web page)
# JustPy uses the quasar framework built with Javascript that is why it is called as Quasar page

def app():
    wp = jp.QuasarPage()        # Create a variable (Component) which contains Quasar page instance
    h1=jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")      # Add elements that this page is going to contain. QDiv = Quasar Division
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")
    

    return wp

jp.justpy(app)      # justpy is a function and it expects as input a function that returns a quasar page