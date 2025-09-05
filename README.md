tock Data API
This is a simple Flask-based API that provides real-time stock information by leveraging the yfinance library. The API is designed to be consumed by a web application, providing stock details and a list of available tickers from the Stockholm stock exchange.

Features
CORS Enabled: The API includes CORS headers, allowing it to be securely accessed from a front-end application hosted on a different domain.

Stock List Endpoint: A static endpoint that returns a list of pre-defined stock tickers and their corresponding names, ideal for search functionality.

Stock Details Endpoint: A dynamic endpoint that fetches detailed information, including live price, historical data, and key metrics for a specific stock ticker using the powerful yfinance library.

API Endpoints

1. Get All Stock Names
   Endpoint: /api/stocks/names

Method: GET

Description: Returns a JSON array of all available stock tickers and their names.

Example Response:

JSON

[
{
"ticker": "ABB.ST",
"name": "ABB Ltd"
},
{
"ticker": "ALFA.ST",
"name": "Alfa Laval AB (publ)"
}
]

2. Get Specific Stock Details
   Endpoint: /api/stocks/details/<ticker>

Method: GET

Description: Fetches and returns detailed financial information for a specific stock ticker.

URL Parameter:

ticker (string): The stock symbol (e.g., VOLV-B.ST).

Example Response:

JSON

{
"ticker": "VOLV-B.ST",
"name": "Volvo AB (publ)",
"change": 1.5,
"price": 250.75,
"currency": "SEK",
"metrics": {
"market_cap": 500000000000,
"trailing_pe": 15.2,
"forward_pe": 14.8,
"peg_ratio": 1.2,
"ps_ratio": 2.5,
"pb_ratio": 3.0,
"ev_revenue": 2.8,
"ev_ebitda": 10.5
},
"priceHistory": [248.5, 249.2, 250.75]
}
Getting Started
Prerequisites
Python 3.x

pip (Python package installer)

Installation
Clone this repository:

Bash

git clone <your-repository-url>
cd <your-repository-name>
Install the required Python packages:

Bash

pip install -r requirements.txt
Note: Your requirements.txt file should include Flask, Flask-CORS, and yfinance.

Run the application:

Bash

python app.py
The server will start on http://0.0.0.0:5000 by default.

Deployment
The application is configured to be deployed on platforms like Render or Heroku. It listens on a dynamic port provided by the environment, ensuring compatibility with most hosting services.

Python

if **name** == '**main**': # Get the port from the environment, defaulting to 5000
port = int(os.environ.get("PORT", 5000)) # Run the app, binding to 0.0.0.0 to accept external requests
app.run(host='0.0.0.0', port=port, debug=True)
