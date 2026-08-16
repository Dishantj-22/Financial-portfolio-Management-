# Financial Portfolio Tracker

A Python command-line application for tracking stock holdings, fetching live market prices, calculating portfolio value, and visualizing portfolio composition — built with modular design principles.

## Features

- **Portfolio Management** — add, remove, and update stock holdings by ticker symbol
- **Live Price Fetching** — pulls real-time closing prices via [yfinance](https://github.com/ranaroussi/yfinance)
- **Portfolio Analysis** — calculates total value and per-stock value breakdown
- **Visualization** — generates a bar chart of stock values using matplotlib
- **Modular Architecture** — clean separation between UI, business logic, and data layers

## Project Structure

```
financial-portfolio-tracker/
├── main.py                 # Entry point — orchestrates the workflow
├── portfolio_management.py # Portfolio class (add/remove/update/get holdings)
├── data_fetcher.py         # Live price fetching via yfinance
├── analysis.py              # Portfolio value calculations
├── visualization.py         # Bar chart generation via matplotlib
├── requirements.txt
├── .gitignore
└── README.md
```

## Architecture

```
User Interface Layer   (main.py)
        ↓
Business Logic Layer   (analysis.py, portfolio_management.py)
        ↓
Data Layer              (data_fetcher.py)
        ↓
External APIs            (yfinance)
```

| Module | Responsibility |
|---|---|
| `portfolio_management.py` | Manage portfolio data (add, remove, update stocks) |
| `data_fetcher.py` | Fetch live stock prices from the yfinance API |
| `analysis.py` | Calculate portfolio value and metrics |
| `visualization.py` | Generate charts and graphs |
| `main.py` | Orchestrate workflow and user interaction |

## Requirements

- Python 3.9+
- See `requirements.txt` for package dependencies

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd financial-portfolio-tracker

# (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run the application from the project root:

```bash
python main.py
```

You'll be prompted to enter stock tickers and quantities one at a time:

```
Enter your portfolio stocks (type 'done' when finished):
Stock ticker symbol: AAPL
Quantity owned: 10
Stock ticker symbol: MSFT
Quantity owned: 5
Stock ticker symbol: done

Fetching live stock prices...

Current Stock Prices:
AAPL: $189.23
MSFT: $412.87

Total portfolio value: $3,956.65
```

A bar chart of your portfolio's stock values will then open in a new window.

## Known Issue / Fix Applied

The original source had a filename mismatch: `main.py` imports `from visualization import plot_portfolio`, but the chart module was saved as `visualition.py` (typo), which causes an `ImportError` on the module load. This repo includes a corrected `visualization.py` — make sure only that correctly named file is present (delete or rename any `visualition.py`).

## Error Handling

The application handles:
- Non-integer quantity input
- Empty portfolios (exits gracefully with a message)
- Missing/unavailable ticker prices (defaults to `0`)
- Network/API errors during price fetching (wrap `fetch_live_prices` calls in `try/except` if you extend this)

## Roadmap / Future Enhancements

- Historical price tracking and performance trending
- Portfolio diversification analysis
- GUI (Tkinter or PyQt)
- Persistent storage via a database
- Portfolio comparison and dividend/income tracking
- Support for multiple asset classes (bonds, crypto, etc.)
- Automated report generation and price-threshold alerts

## Tech Stack

- **Python 3.x** — core language
- **yfinance** — live market data
- **pandas** — data handling
- **matplotlib** — visualization
- **requests** — HTTP (used internally by yfinance)

## License

