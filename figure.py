from  matplotlib.figure import Figure
from matplotlib import use as set_backend
from io import BytesIO
import base64

set_backend("agg")

def create_figure(data, theta=None):
    x = data[:,0]
    y = data[:,1]
    fig = Figure()   #Avoiding PyPlot because it's prone to memory leaks
    ax = fig.subplots()
    ax.scatter(x,y)

    if theta is not None:
        ax.axline((0,theta.item(0)), slope = theta.item(1), color="r")

    stream = BytesIO()
    fig.savefig(stream, format="png")
    figure = base64.b64encode(stream.getbuffer()).decode("ascii")

    return figure