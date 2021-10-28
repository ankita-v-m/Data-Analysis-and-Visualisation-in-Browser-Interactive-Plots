import justpy as jp
from pandas.core.dtypes.common import classes

# Every JustPy app will have a main object that is known as a Quasar page (Web page)

def app():
    wp = jp.QuasarPage()
    h1=jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")

    return wp

jp.justpy(app)