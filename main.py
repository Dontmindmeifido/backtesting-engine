from config.config import config
from signal import get_signal
from exchange import slippage
from exchange import fee
from performance import sharpe
import math
import pandas
import matplotlib.pyplot as plt

# Initialize Market Data
asset_path = "BTC-1m.csv"
ohlc = pandas.read_csv(asset_path, usecols = [1, 2, 3, 4]).values.tolist()[-60*24*360: -1]

close = [i[3] for i in ohlc]
open = [i[0] for i in ohlc]
log_return = [math.log(i[3]/i[0]) for i in ohlc]

# Initialize Entry
signal = get_signal([j[3]/2 + j[0]/2 for j in ohlc], config["fast"], config["slow"], plot=False)

# Cumulative returns
cumulative_return = [0]
    

if __name__ == "__main__":
    # Computer cumulative returns
    for i in range(len(close)): 
        cumulative_return.append(cumulative_return[-1] + signal[i]*log_return[i] - slippage(config["slippage"]) - fee(config["fee"]))

    # Performance metrics
    sharpe_ = sharpe(cumulative_return, "minute")

    #Visuals
    plt.xlabel("Trades")
    plt.ylabel("Strategy Log Return")

    plt.plot(cumulative_return, c="red", label=f"Cumulative Return \n Sharpe: {(sharpe_ * 100) // 1 / 100}")
    plt.legend()
    plt.show()

