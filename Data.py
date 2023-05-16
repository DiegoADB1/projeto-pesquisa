from datetime import datetime
import pandas as pd
import pytz
from pandas.plotting import register_matplotlib_converters
import MetaTrader5 as mt5
import json

register_matplotlib_converters()

# connect to MetaTrader 5
jsonConfig = open("config.json")
config = json.load(jsonConfig)
if not mt5.initialize(login=config["login"], server="MetaQuotes-Demo", password=config["password"]):
    print("initialize() failed")
    mt5.shutdown()

timezone = pytz.timezone("UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with data")
print(rates_frame)
