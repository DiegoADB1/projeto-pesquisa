import pandas as pd
import plotly.graph_objects as go


def createCandleGraph(data: pd.DataFrame):
    # Creates graph based on received data
    graph = go.Figure(data=[go.Candlestick(x=data['time'],
                                           open=data['open'],
                                           high=data['high'],
                                           low=data['low'],
                                           close=data['close'])])
    # Shows the graph in your browser
    graph.show()
