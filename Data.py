from datetime import datetime
import pandas as pd
import pytz
from pandas.plotting import register_matplotlib_converters
import MetaTrader5 as mt5
import json
from Graph import createCandleGraph

register_matplotlib_converters()

# get login and password from another file
jsonConfig = open("config.json")
config = json.load(jsonConfig)

# connect to MetaTrader 5
if not mt5.initialize(login=config["login"], server="OramaDTVM-Server", password=config["password"]):
    print("initialize() failed")
    mt5.shutdown()

timezone = pytz.timezone("UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone - TIMEFRAME_H4 = each 4 hours
rates = mt5.copy_rates_from("PETR4", mt5.TIMEFRAME_D1, utc_from, 5000)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# displays data as a candle graph
createCandleGraph(rates_frame)
