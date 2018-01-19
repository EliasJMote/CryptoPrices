# Run this program to create a time-stamped file displaying the last
# prices of several crypto coins (BTC, ETH, LTC)

from bittrex.bittrex import Bittrex, API_V1_1
from datetime import *
import json
from shutil import copyfile
import os

# my_bittrex variable holds market data from Bittrex
my_bittrex = Bittrex(None, None, api_version=API_V1_1)

# Create a dictionary to hold coin data
coin_data = {}

# Get data from the coins (in USDT markets for easier comparison)
USDT_BTC = (my_bittrex.get_marketsummary('USDT-BTC'))
USDT_ETH = (my_bittrex.get_marketsummary('USDT-ETH'))
USDT_LTC = (my_bittrex.get_marketsummary('USDT-LTC'))

# Add the coin data to the dictionary
coin_data["USDT_BTC_LAST"] = USDT_BTC[u'result'][0][u'Last']
coin_data["USDT_ETH_LAST"] = USDT_ETH[u'result'][0][u'Last']
coin_data["USDT_LTC_LAST"] = USDT_LTC[u'result'][0][u'Last']

# Create a json array with the coin data dictionary
d = coin_data
json_array = json.dumps(d)

# Create a file name based on current timestamp
filename = datetime.now().strftime("%Y-%m-%d_%H:%M_Report.txt")

# Use relative directory CoinReports to place coin data reports
dir = os.path.dirname(__file__)

# If the coin reports directory does not exist, create it 
if not os.path.exists(dir + "/Coin_Reports/"):
    os.makedirs(dir + "/Coin_Reports")


fo = open(dir + "/Coin_Reports/" + filename, "w")

fo.write(str(coin_data))

fo.close()

