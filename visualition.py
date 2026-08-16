import matplotlib.pyplot as plt


def plot_portfolio(stock_values):
    """Render a bar chart of stock values in the portfolio."""
    tickers = list(stock_values.keys())
    values = list(stock_values.values())

    plt.bar(tickers, values, color='skyblue')
    plt.title('Portfolio Stock Values')
    plt.ylabel('Value in USD')
    plt.xlabel('Stock Ticker')
    plt.show()