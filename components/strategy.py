from lumibot.strategies.strategy import Strategy

class MyStrategy(Strategy):
    def initialize(self):
        self.sma_short = 10
        self.sma_long = 30

    def on_trading_iteration(self):
        data = self.get_historical_data("AAPL", "1d", limit=self.sma_long)
        short_sma = data['close'][-self.sma_short:].mean()
        long_sma = data['close'][-self.sma_long:].mean()

        if short_sma > long_sma:
            self.buy("AAPL", quantity=10)
        elif short_sma < long_sma:
            self.sell("AAPL", quantity=10)
