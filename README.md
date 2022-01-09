# trading_bot_local

tradingbot_local is a Python discord bot for options/stock traders to alert easily in multiple servers.
It is a slightly modified version of [tradingbot](https://github.com/js430/tradingbot.git)
## Installation

Use git clone or your choice of repository cloning to pull the repo

```bash
git clone https://github.com/js430/trading_bot_local.git
```

## Usage

```python
!python tradingbot.py

#buy signal
#parameters: date, ticker, strike price, call/put, price, max # of cons (optional), image link (optional)

!buy 1/6 SPY 480 C .65 cons=None image=None

# sell signal
#parameters: date, ticker, strike price, call/put, price, image link (optional)
!buy 1/6 SPY 480 C .65 image=None

#trim signal
#parameters: ticker, price
!trim SPY .56

#cut signal
#parameters: ticker, price
!cut SPY .56

#msg
#parameters: message, image(optional)
!msg txt image=None

```

## Contributing
Pull requests are welcome, if you want a copy of the bot for your own use, feel free or contact me @ jeffreyshi430@gmail.com if you wish for me to make you a version with your
specifications/capabilities.

## License
[MIT](https://choosealicense.com/licenses/mit/)