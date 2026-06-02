# Binance Futures Trading Bot

## Overview

A Python-based trading bot built for Binance Futures Demo/Testnet.

The application supports:

- Market Orders
- Limit Orders
- BUY Orders
- SELL Orders
- Command Line Interface (CLI)
- Input Validation
- Logging
- Exception Handling

## Project Structure

```
TradingBotAssignment/

├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository_url>
cd TradingBotAssignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Credentials

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Usage

### Place Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

## Features Implemented

- Binance Futures Demo/Testnet Integration
- Market Order Placement
- Limit Order Placement
- BUY and SELL Support
- CLI Input Validation
- Structured Project Design
- Logging of Requests and Responses
- Exception Handling

## Logging

All API requests, responses, and errors are stored in:

```
logs/trading.log
```

Example log entries:

```text
REQUEST => BUY MARKET BTCUSDT
RESPONSE => Order Successfully Created

REQUEST => SELL LIMIT BTCUSDT
RESPONSE => Order Successfully Created
```

## Technologies Used

- Python 3
- Requests
- python-dotenv
- Binance Futures Demo API

## Assumptions

- User has valid Binance Futures Demo/Testnet API credentials.
- Futures trading permission is enabled for the API key.
- Internet connection is available.